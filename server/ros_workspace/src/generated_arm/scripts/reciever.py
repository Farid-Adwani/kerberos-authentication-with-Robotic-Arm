import socket
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5000     # Use a non-reserved port number
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_reciever', anonymous=True)
robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "arm"
group = moveit_commander.MoveGroupCommander(group_name)

def move_arm():
    # Get a random valid pose
    pose_goal = group.get_random_pose().pose

    # Set the pose target
    group.set_pose_target(pose_goal)

    # Plan and execute the trajectory
    plan = group.go(wait=True)
    group.stop()
    group.clear_pose_targets()

# Create a socket object
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to a specific address and port
        s.bind((HOST, PORT))
        # Listen for incoming connections
        s.listen()
        print('Waiting for a connection...')

        # Accept a connection
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            # Keep receiving data in a loop
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                if(data.decode()=="move"):
                    move_arm()
