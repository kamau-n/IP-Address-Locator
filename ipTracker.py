#!/usr/bin/env/python3

from tkinter import *
from tkinter import messagebox
import geocoder


root=Tk()
root.title("ip tracker")

def track():
    text.delete('1.0','end-1c')
    ip=entry.get()
    global location
    location=geocoder.ip(ip)
    city=location.city
    country=location.country
    longitude=str(location.lng)
    latitude=str(location.lat)
    area=location.street
    print(area)
    status=location.ok

    #incase of wrong ip address
    if not status:
        message=messagebox.showerror("ERROR MESSAGE","ip not found")
        text.delete('1.0','end-1c')
        
        
    

    
    text.insert('1.0',"City : " +city +"\n")
    text.insert('end',"Coutry : "+country +"\n")
    text.insert('end',"Longitude : "+longitude+"\n")
    text.insert('end',"Longitude : "+latitude+"\n")
  
label =Label(root,text="MY IP TRACKER")
label.grid(row=0,column=1)

label2=Label(root,text="Enter Your Ip Address")
label2.grid(row=1,column=0)


entry=Entry(root,bd=5)
entry.grid(row=1,column=1,columnspan=1)

button=Button(root,bd=3,text='get',command=track,relief='sunken')
button.grid()

text=Text(root,bd=4,bg='grey',pady=10,padx=30,font=("Terminal Pr", "16"),width=20,height=15)
text.grid(row=2,column=1)
