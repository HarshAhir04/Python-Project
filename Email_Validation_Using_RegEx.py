# a-z wscube@gmail.com
# 0-9
# . _ time 1
# @ time(count)=1
# email[-4] or email[-3] == "."
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Your Email:-\n")
if re.search(email_condition,user_email):
    print(f"Your Email Is Right\nYour Email Is {user_email}")
else:
    print()
