from django.http import HttpResponse,FileResponse
from django.shortcuts import render
import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import mysql.connector
def menu(request):
    return render(request,"login.html")
def verification(request):
    userid=request.POST.get("userid")
    password=request.POST.get("password")
    mydb=mysql.connector.connect(host='vs047-postgres-9300-production',user="root",password=os.environ["DATABASE_PASSWORD"],database="database")
    console=mydb.cursor()
    try:
        console.execute("SELECT *  FROM details WHERE email=%s and password=%s",(userid,password))
        result=console.fetchall()
        if result==[]:
            return render(request,"login.html",{"error":True,"value":"Invalid username and/or password"})
        else:
            return render(request,"selection.html")
    except:
        console.execute("create table details ( ID decimal(10) primary key not null,email varchar(30),password varchar(20))")
def entry(request):
    userid=request.POST.get("userid")
    password=request.POST.get("password")
    mydb=mysql.connector.connect(host='vs047-postgres-9300-production',user="root",password=os.environ["DATABASE_PASSWORD"],database="database")
    console=mydb.cursor()
    console.execute("SELECT * FROM details where email=%s and password=%s",(userid,password))
    result=console.fetchall()
    if result!=[]:
        return render(request,"register.html",{"error":True,"value":"account already exist"})
    else:
        console.execute("SELECT MAX(ID) FROM details")
        idno=console.fetchall()
        console.execute("INSERT INTO details (ID,email,password) values (%s,%s,%s)",(idno[0][0]+1,userid,password))
        mydb.commit()
        return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def select(request):
    return render(request,"selection.html")
def download(request):
    zip_file = open("dist.zip", 'rb')
    response = FileResponse(zip_file)
    return response
def index(request):
    return render(request,"main.html")
def showoutput(request):

    # input variables
    hlength=request.POST.get("hlength",0)
    hdiameter=request.POST.get("hdiameter",0)
    ulength=request.POST.get("ulength",0)
    udiameter=request.POST.get("udiameter",0)
    flength=request.POST.get("flength",0)
    fdiameter=request.POST.get("fdiameter",0)
    tilength=request.POST.get("tilength",0)
    tidiameter=request.POST.get("tidiameter",0)
    talength=request.POST.get("talength",0)
    tadiameter=request.POST.get("tadiameter",0)
    try:
        if int(hlength)<=0 or int(hdiameter)<=0 or int(ulength)<=0 or int(udiameter)<=0 or int(flength)<=0 or int(fdiameter)<=0 or int(tilength)<=0 or int(tidiameter)<=0 or int(talength)<=0 or int(tadiameter)<=0:
            errormessage={"error":True}
            return render(request,"main.html",errormessage)
    except:
        errormessage={"error":True}
        return render(request,"main.html",errormessage)
    #model training
    data=pd.read_csv("dataset/bird.csv")
    data.dropna(inplace=True)
    x_train,x_test,y_train,y_test=train_test_split(data.loc[:,"huml":"tarw"],data["type"],test_size=0.25,random_state=0)
    ss=StandardScaler()
    x_train=ss.fit_transform(x_train)
    x_test=ss.fit_transform(x_test)
    model=SVC(C=100,kernel="linear")
    model.fit(x_train,y_train)
    
    cateogary={"SW":"Swimming birds","W":"Wading birds","T":"Terristrial birds","R":"Raptors","P":"Scansorial birds","SO":"Singing birds"}
    prediction=model.predict([[hlength,hdiameter,ulength,udiameter,flength,fdiameter,tilength,tidiameter,talength,tadiameter]])
    answers={"value":f"The bird belongs to {cateogary[prediction[0]]} cateogary","correct":True}
    return render(request,"main.html",answers)
    # return HttpResponse(f"The bird belongs to {cateogary[prediction[0]]} cateogary")
