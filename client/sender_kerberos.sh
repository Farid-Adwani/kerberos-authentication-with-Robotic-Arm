klist -s
if [ $? -eq 0 ]
then
    echo "Valid Kerberos TGT found"
    python3 sender.py
else
    echo "No valid Kerberos TGT found"
    echo "Please enter Your Password and restart"
    kinit
fi
