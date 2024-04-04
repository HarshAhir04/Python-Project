email=input("Enter Your Email:-")#g@g.in or g@g.com
j,k,l=0,0,0
j,k,l=0,0,0
if len(email)>=6:#1
    if email[0].isalpha():#2
        if ("@" in email) and (email.count("@")==1):#3
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        j==1
                    elif i==i.upper():
                        k==1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        l==1
                if k==1 or j==1 or l==1:
                    print("Wrong Email 5")
                else:
                    print(f"your Email is Right\nYour Email is {email}")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")