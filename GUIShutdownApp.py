from tkinter import *
import os
def restrat():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")
st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="pink")

r_button=Button(st,text="Restart",font=("time new Romen",20,"bold"),
                relief=RAISED,cursor="plus",command=restrat)
r_button.place(x=150,y=60,height=40,width=200)

rt_button=Button(st,text="Restart Time",font=("time new Romen",20,"bold"),
                 relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=40,width=200)

lg_button=Button(st,text="Log-Out",font=("time new Romen",20,"bold"),
                 relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=40,width=200)

st_button=Button(st,text="Shutdown",font=("time new Romen",20,"bold"),
                 relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=40,width=200)

st.mainloop()
