# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:43:32 2020

@author: KapilMangla
"""

import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
import datetime



#Function to display Frames on Tkinter  UI
def videost():
    ret,frame = cap.read()
    if (togglevar.get()==1):
        faces=face_cascade.detectMultiScale(frame ,1.1 ,4)
        for (x, y, w, h) in faces:
            cv.rectangle(frame ,(x,y) ,(x+w ,y+h) ,(255,0,0) ,0)
    else:
        pass
    img=cv.cvtColor(frame ,cv.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(img,master=root)
    Label1.imgtk=imgtk
    Label1.configure(image=imgtk)
    Label1.after(35, videost)


#Function to record video
def record():
    r,f=cap.read()
    if r==True:
        out.write(f)
        root.after_idle(record)
    
#Function to use video button for both start and stop recording    
def video_rec():
    
    global out
    
    datet=str(datetime.datetime.now())
    date=datet.split(".")
    date=date[0].replace("-","")
    date=date.replace(":","")
    date=date.replace(" ","")
    
    x=video_var.get()
    if(x == 'Start Recording'):
        
        out=cv.VideoWriter(f'VID{date}.avi', fourcc, 10.0, (640,480)) 
        video_var.set("Stop")
        record()
       
    else: 
        out.release()
        t="Start Recording"
        video_var.set(t)
        
    
        
#Function to capture image     
def capture():
    r,f=cap.read()
    cv.imwrite(f"{Label1['image']}.jpg",f)
    cv.imshow(f"{Label1['image']}",f)
    cv.waitKey(0)
    cv.destroyAllWindows()
    

    
    
 
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
fourcc=cv.VideoWriter_fourcc(*'XVID') 



#Code for UI
root=Tk()

root.geometry("840x580")
root.minsize(840,580)
root.maxsize(840,580)
root.configure(bg="powder blue")

l1=Label(root,text="Audio and Video Capture using OpenCV & Tkinter",bg="red",font="comicsansms 15 bold", borderwidth=5, relief=SUNKEN)
l1.pack(pady=5,fill=X)
l2=Label(root,text="By -- Kapil Mangla",font="comicsanms 10 bold",bg="powder blue")
l2.pack()
Label1=Label(root,bg="powder blue")
Label1.place(x=0,y=70,width=840,height=380)

Fl=Label(root,text="Detect Face",font="comicsanms 10 bold",bg="powder blue").place(x=400,y=470)

#RadioButton for toggling face detection
togglevar=IntVar()
rb1 = Radiobutton(root, text="ON ", variable=togglevar, value=1, indicatoron=0).place(x=410,y=500)
rb1 = Radiobutton(root, text="OFF ", variable=togglevar, value=0, indicatoron=0).place(x=440,y=500)

    
#Button for image capture
Cap_button=Button(root, text="Capture Image",command=capture).place(x=200,y= 470)

#Button for video capture
video_var=StringVar()
video_button=Button(root,textvariable=video_var,command= video_rec).place(x=600,y= 470)    
video_var.set("Start Recording")


cap=cv.VideoCapture(0)
videost()  


 
root.mainloop()  
cap.release() 
cv.destroyAllWindows()
    