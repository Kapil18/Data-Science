# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:30:47 2020

@author: KapilMangla
"""

import json
import pickle
import numpy as np
import tkinter.messagebox as tmsg


numlist=["One","Two","Three","Four","Five"]
locations=None
data_columns=None
model=None

#Loading locations from json file
with open("columns.json",'r') as f:
        data_columns=json.load(f)['data_columns']
        locations= data_columns[3:]
        
#Loading Linear regression model
with open("bangalore_home_prices_model.pickle",'rb') as f:
        model=pickle.load(f)
        
        
        
       
#Function for button
        
def predict_price():
    location=locdrop.get()
    sqft=Area.get()
    bath=var2.get()
    bhk=var1.get()
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    price=round(model.predict([x])[0],2)
    tmsg.showinfo("Estimated Price", f"The home you are looking will cost around {price} Lakhs ₹")
    
        
## Creating GUI
        
from tkinter import *
from tkinter import ttk

root=Tk()

root.geometry("840x480")

root.minsize(840,480)
root.maxsize(840,480)



l1=Label(root,text="Bangalore Home Price Prediction",bg="red",font="comicsansms 15 bold", borderwidth=5, relief=RIDGE)
l1.pack(pady=5)

#GUI for AREA
Label(root,text="Area (In Square Feet)",bg='light blue',font="comicsansms 10 bold").place(x=365,y=60)
Area = Scale(root, from_=500, to=3000, orient=HORIZONTAL, tickinterval=500)
Area.place(x=20,y=80,width=800)

#GUI for BHK
var1 = IntVar()
var1.set(3)
Label(root,text="BHK",bg='light blue',font="comicsansms 10 bold").place(x=20,y=170)
pos=130
for i,j in enumerate(numlist):
    bhk = Radiobutton(root, text=j, padx=14, variable=var1, value=i+1).place(x=pos,y=170)
    pos=pos+100

#GUI for Bath
var2 = IntVar()
var2.set(1)
Label(root,text="BATH",bg='light blue',font="comicsansms 10 bold").place(x=20,y=230)
pos=130
for i,j in enumerate(numlist):
    bath = Radiobutton(root, text=j, padx=14, variable=var2, value=i+1).place(x=pos,y=230)
    pos=pos+100
    
#GUI for Locations
Label(root,text="Choose Your Location",bg='light blue',font="comicsansms 10 bold").place(x=20,y=300)
locdrop=ttk.Combobox(root,values=locations)
locdrop.set("Choose")
locdrop.place(x=350,y=300,width=200)


#Button
b1 = Button(root, text="Estimate Price ",command=predict_price)
b1.place(x=400,y=400 )


root.mainloop()