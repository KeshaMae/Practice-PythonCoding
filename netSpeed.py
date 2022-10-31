from tkinter import *
import speedtest 

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("700x700")
sp.config(bg="Black")

lab = Label(sp,text=" Internet Speed Test ", font=("Georgia",30,"bold"),bg="Black",fg="White")
lab.place(x=70,y=50,height=60,width=580)

lab = Label(sp,text="Download Speed", font=("Georgia",30,"bold"),bg="Black",fg="White")
lab.place(x=70,y=140,height=60,width=580)

lab_down = Label(sp,text="00", font=("Georgia",30,"bold"))
lab_down.place(x=70,y=210,height=60,width=580)

lab = Label(sp,text="Upload Speed", font=("Georgia",30,"bold"),bg="Black",fg="White")
lab.place(x=70,y=300,height=60,width=580)

lab_up = Label(sp,text="00", font=("Georgia",30,"bold"))
lab_up.place(x=70,y=370,height=60,width=580)

button = Button (sp,text="Check Speed", font=("Georgia",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
button.place(x=70,y=470,height=60,width=580)

sp.mainloop()