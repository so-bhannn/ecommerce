from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method=='POST':
        username=username.POST['username']
        fname=fname.POST['fname']
        lname=lname.POST['lname']
        email=email.POST['email']
        pass1=pass1.POST['pass1']
        pass2=pass2.POST['pass2']
        
        myuser=User.object.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        return redirect('login')



def login(request):
    loggedin=request.GET.get("loggedin","off")


    
    return render(request, 'authentication/login.html')