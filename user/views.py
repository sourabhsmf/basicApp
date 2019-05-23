from django.shortcuts import render,HttpResponse
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
                    return HttpResponse("<h1>Welcome {}</h1>".format(unauthenticatedUser.email))
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
