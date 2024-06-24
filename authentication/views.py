from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
import pyrebase
import os
from dotenv import load_dotenv

# Create your views here.

load_dotenv()

config={
    "apiKey":os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL":os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId":os.getenv("FIREBASE_MESSAGING_SENDER_ID") ,
    "appId": os.getenv("FIREBASE_APP_ID"),
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()

def home(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'authentication/signup.html')

def login(request):  
    return render(request,'authentication/login.html')

def logout(request):
    try:
        del request.session['idToken']
    except:
        pass
    return render(request,'services/index.html')

def postsignup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if pass1!=pass2:
            messages.error(request, "Passwords Didn't match.")
            return redirect('signup')

        if len(username)>20:
            messages.error(request, "Username too long.")
            return redirect('signup')

        # if not username.isalnum():
        #     messages.error(request, "Username should contain letters, numbers and special characters.")
        #     return redirect('signup')
        try:
            user=auth.create_user_with_email_and_password(email,pass1)
            idToken=request.session[user['localId']]
        except:
            message="Account cannot be made now, try again after some time."
            return render(request,'authentication/signup.html',{"alert":message})
        return render(request,'authentication/login.html',{'msg':message})
    return render(request,'authentication/signup.html')

def postlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('passw')
        try:
            user=auth.sign_in_with_email_and_password(email,pass1)
            request.session['uid']=str(user['idToken'])
        except:
            message="Invalid Credentials"
            return render(request,'authentication/login.html',{'alert':message})    
    return render(request, 'services/index.html',{"email":email})