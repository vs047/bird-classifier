from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
class UI:
    def __init__(self):
        self.window=Tk()
        self.window.geometry('700x700')
        self.window.resizable(False,False)
        self.background=PhotoImage(file='images/background.png')
        self.icon=PhotoImage(file="images/icon.png")
        self.window.iconphoto(True,self.icon)
        self.canvas=Canvas(self.window,width=800,height=800)
        self.canvas.pack()
        self.window.title("Bird Classifier")
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="birdlogin")
        console=mydb.cursor()
        self.window.withdraw()
        self.email=simpledialog.askstring("login","enter login email")
        self.password=simpledialog.askstring("login","enter password",show="*")
        console.execute("SELECT *  FROM details WHERE email=%s and password=%s",(self.email,self.password))
        result=console.fetchall()
        console.execute("SELECT MAX(ID) from details")
        pkey=console.fetchall()
        self.canvas.create_image(0,0,anchor=NW,image=self.background)
        self.Humeruslength,self.Humerusdiameter,self.Ulnalength,self.Ulnadiameter,self.Femurlength,self.Femurdiameter=DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window)
        self.Tibiotarsuslength,self.Tibiotarsusdiameter,self.Tarsometatarsuslength,self.Tarsometatarsusdiameter=DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window)
        Label(self.window,text="Bird Classifier",font=("Times New Roman ",30),fg="orange",bg="black").place(relx=0.3,rely=0)
        
        Entry(self.window,textvar=self.Humeruslength,font=("Times New Roman",15)).place(relx=0.5,rely=0.2)
        Label(self.window,text="Enter length of Humerus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.2)

        Label(self.window,text="Enter length of  Ulna",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.25)
        Entry(self.window,textvar=self.Ulnalength,font=("Times New Roman",15)).place(relx=0.5,rely=0.25)
        
        Label(self.window,text="Enter length of  Femur",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.3)
        Entry(self.window,textvar=self.Femurlength,font=("Times New Roman",15)).place(relx=0.5,rely=0.3)
        
        Label(self.window,text="Enter length of  Tibiotarsus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.35)
        Entry(self.window,textvar=self.Tibiotarsuslength,font=("Times New Roman",15)).place(relx=0.5,rely=0.35)
        
        Label(self.window,text="Enter length of  Tarsometatarsus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.4)
        Entry(self.window,textvar=self.Tarsometatarsuslength,font=("Times New Roman",15)).place(relx=0.5,rely=0.4)

        Label(self.window,text="enter diameter of Humerus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.45)
        Entry(self.window,textvar=self.Humerusdiameter,font=("Times New Roman",15)).place(relx=0.5,rely=0.45)

        Label(self.window,text="Enter diameter of Ulna",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.5)
        Entry(self.window,textvar=self.Ulnadiameter,font=("Times New Roman",15)).place(relx=0.5,rely=0.5)

        Label(self.window,text="Enter diameter of Femur",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.55)
        Entry(self.window,textvar=self.Femurdiameter,font=("Times New Roman",15)).place(relx=0.5,rely=0.55)

        Label(self.window,text="Enter diameter of Tibiotarsus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.6)
        Entry(self.window,textvar=self.Tibiotarsusdiameter,font=("Times New Roman",15)).place(relx=0.5,rely=0.6)

        Label(self.window,text="Enter diameter of Tarsometatarsus",bg="red",fg="white",font=("Times New Roman",15)).place(relx=0,rely=0.65)
        Entry(self.window,textvar=self.Tarsometatarsusdiameter,font=("Times New Roman",15)).place(relx=0.5,rely=0.65)

        Button(self.window,text="Generate Model",fg="orange",bg="black",command=self.generatemodel,font=("Times New Roman",20)).place(relx=0.2,rely=0.8)
        Button(self.window,text="Predict Result",fg="orange",bg="black",command=self.predict,font=("Times New Roman",20)).place(relx=0.6,rely=0.8)
        Button(self.window,text="Clear values",fg="orange",bg="black",command=self.reset,font=("Times New Roman",20)).place(relx=0.4,rely=0.9)
        if result==[]:
            messagebox.showerror("Error","No such account exist")
            choice=messagebox.askquestion("Action","Do you want to register")
            if choice=="yes":
                self.email=simpledialog.askstring("login","enter  email for registration")
                self.password=simpledialog.askstring("login","enter password",show="*")
                console.execute("INSERT INTO details (ID,email,password) values (%s,%s,%s)",(pkey[0][0]+1,self.email,self.password))
                mydb.commit()
            else:
                self.window.destroy()
        try:
            self.window.deiconify()
        except:
            pass
        self.window.mainloop()
    def reset(self):
        self.Humeruslength.set(0)
        self.Humerusdiameter.set(0)
        self.Ulnalength.set(0)
        self.Ulnadiameter.set(0)
        self.Femurlength.set(0)
        self.Femurdiameter.set(0)
        self.Tibiotarsuslength.set(0)
        self.Tibiotarsusdiameter.set(0)
        self.Tarsometatarsuslength.set(0)
        self.Tarsometatarsusdiameter.set(0)    
    def generatemodel(self):
        data=pd.read_csv("dataset/bird.csv")
        data.dropna(inplace=True)
        x_train,x_test,y_train,y_test=train_test_split(data.loc[:,"huml":"tarw"],data["type"],test_size=0.25,random_state=0)
        ss=StandardScaler()
        x_train=ss.fit_transform(x_train)
        x_test=ss.fit_transform(x_test)
        self.model=SVC(C=100,kernel="linear")
        self.model.fit(x_train,y_train)
        messagebox.showinfo("information","model generated successfully")
    def predict(self):
        try:
            inputs=[self.Humeruslength.get(),self.Humerusdiameter.get(),self.Ulnalength.get(),self.Ulnadiameter.get(),self.Femurlength.get(),self.Femurdiameter.get(),self.Tibiotarsuslength.get(),self.Tibiotarsusdiameter.get(),self.Tarsometatarsuslength.get(),self.Tarsometatarsusdiameter.get()]
            for i in inputs:
                if i<0:
                    messagebox.showerror("Fatal Error","dimensions cannot be negative")
                    return 
            output=self.model.predict([inputs])
            cateogary={"SW":"Swimming birds","W":"Wading birds","T":"Terristrial birds","R":"Raptors","P":"Scansorial birds","SO":"Singing birds"}
            messagebox.showinfo("Result",f"The bird belongs to {cateogary[output[0]]} cateogary")
        except:
            messagebox.showerror("Fatal Error","Model not created")
sample=UI()
