from django.shortcuts import render,redirect,HttpResponse
from .models import student
from django.contrib import messages

# Create your views here.
def index(request):
		return render(request,"index.html")

# student registion
def register(request):
		return render(request,"register.html")


def save_data(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        city= request.POST["city"]
        contact=request.POST["contact"]

        app=student(fname=fname,lname=lname,email=email,password=password,city=city,contact=contact)
        app.save()  #insert

        #return HttpResponse("Register succfull")
        messages.success(request,"Register Sucessfully Completed")
        return render(request,"login.html")
    else:
        messages.warning(request,"Login Fail")
        return redirect("/register")
        


# Student login		
def login1(request):
		return render(request,"login.html")

def login_check(request):
    if request.method=="POST":
        email= request.POST["email"]
        password=request.POST["password"]

        data = student.objects.all().filter(email=email,password=password)

       # if len(data)==1:
        if data:
            request.session["username"]=email   # session strt
            messages.success(request,"Login Sucessfully Completed")
            return redirect("/dashboard")
        else:
            messages.warning(request,"Login Fail")
            return redirect("/login1")

def dashboard(request):
    if request.session.get("username") is not None:
       return render(request,"dashboard.html")
    else:
        return redirect("/login1")

# student Logout
def logout1(request): 
    del request.session["username"] #session end
    messages.info(request,"Logout Sucessfully Completed")
    return redirect("/login1")   

# welcome page
def welcome(request):
    data=student.objects.all()   # select
    return render(request,"welcome.html",{'data':data})

#delete data   
def delete(request):
    id=request.GET["id"]
    student.objects.filter(id=id).delete() #delete
    return redirect("/welcome")   

#update data
def edit(request):
    id=request.GET["id"]
    data = student.objects.all().filter(id=id)
    return render(request,"edit.html",{'data':data})   

def update(request):
    if request.method=="POST":
        id=request.POST["id"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        city= request.POST["city"]
        contact=request.POST["contact"]

        # update
        student.objects.filter(id=id).update(fname=fname,lname=lname,email=email,password=password,city=city,contact=contact)
        
        messages.info(request,"Updated Sucessfully Completed")
        return redirect("/welcome")
    else:
        messages.warning(request,"Fail")
        return redirect("/welcome")

def form(request):

    form=customerform()

    return render(request,"form.html" , {'form':form})



#**************************************Authantication**********************************************************

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

# register user admin authantication
def auth_registration(request):
     return render(request,"auth_registration.html" )

def auth_save(request):
    if request.method == "POST":
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["email"]
            password = request.POST["password"]

            au=User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname)
            au.save()

            messages.success(request,"Successfully Registion")
            return redirect("/auth_login")
    else:
             messages.warning(request,"Fail")
             return redirect("/auth_registration")



# login user admin authantication
def auth_login(request):
     return render(request,"auth_login.html" )

def auth_login_check(request):
    if request.method=="POST":
        email=request.POST["email"]  
        password=request.POST["password"]   

        au=authenticate(username=email,password=password)

        if au:
            login(request,au) #session start
            return redirect("/welcome")
        else:
            messages.warning(request,"Login Faill")
            return redirect("/auth_login") 
    else:
        messages.success(request,"Login Sucessfully Completed")
        return render(request,"auth_login.html")
        

# logout
def auth_logout(request):
    logout(request) #session end
    messages.success(request,"Logout Sucessfully ")
    return redirect("/")

# reset Password
def reset(request):
    return render(request,"reset.html" )

def reset_pass(request):
    if request.method=="POST":
        email=request.POST["email"]  
        old_password=request.POST["old_password"] 
        new_password=request.POST["new_password"]   

        au=authenticate(username=email,password=old_password)

        if au:
            au.set_password(new_password)
            au.save()
            return HttpResponse("Password Update Successfully")
        else:
            return HttpResponse("incorect old password")
    else:
        return render(request,"reset.html")
		