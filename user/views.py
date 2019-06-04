from django.shortcuts import render,HttpResponse,redirect
from django.core import serializers
from .forms import registrationForm,loginForm
from .models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            newUser = User(email = form.cleaned_data['email'] , password = form.cleaned_data['password'])
            newUser.save()
            return HttpResponse("<h1>Thank you</h1> <a href='../login/'>Sign In</a>")
        else:
            return render(request , "register.html" , context={'form':form})
    else:
        return render(request , "register.html")

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            unauthenticatedUser = User(email = form.cleaned_data['email'] , password = form.cleaned_data['password'])
            if unauthenticatedUser.verify_email(User):
                if unauthenticatedUser.verify_password(User):
                    request.session['userid'] = User.objects.get(email=unauthenticatedUser.email).id
                    return redirect('/user/home')
                else:
                    form.add_error('password' , 'Incorrect password')
                    return render(request , 'login.html' , context={'form':form})
            else:
                form.add_error('email' , 'No such user')
                return render(request , 'login.html', context={'form':form})
        else:
            return render(request , "login.html" , context={'form':form})
    else:
        return render(request , 'login.html')
def home(request):
    if request.method == "GET":
        activeUser = User.objects.get(id = request.session.get('userid'))     
        return render(request , 'home.html' , context={'user' : activeUser})
    else:
        return render(request , 'login.html')

def manage(request):
    if request.method == "GET":
        #Check that user requesting has access or not
        if request.session.get('userid') == 1 :
            allUsers = serializers.serialize('json' , User.objects.all() , fields='email')
            return HttpResponse(allUsers , content_type='application/json')
        else:
            return HttpResponse('{"error" : "Access Denied"}' , content_type='application/json')
    else:
        return HttpResponse('{"error : "Access Denied"}' , content_type='application/json')
    