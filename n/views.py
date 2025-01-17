from django.shortcuts import render
from n.models import contact
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from n.models import contact

def home(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        Contact=contact(email=email,password=password)
        Contact.save()
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")   

def event(request):
    return render(request,"event.html")   

def academics(request):
    return render(request,"academics.html")  



def Director(request):
    return render(request,"Director.html")  

def Teachers(request):
    return render(request,"Teachers.html")  

def Students(request):
    return render(request,"Students.html") 

@login_required
def Studentsadmin(request):
    return render(request,"Studentsadmin.html") 
def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("n:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})#contet.
# Create your views here.
