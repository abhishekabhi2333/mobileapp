from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import User
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserRegForm,LoginForm
from django.views.generic import FormView
from django.contrib.auth import authenticate,login,logout

class Home(TemplateView):
    template_name='home.html'

class UserRegView(CreateView):
    template_name='reg.html'
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('home') 

    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are registered in BlogApp.\n Your username:"+str(uname)+"\n Password:"+str(pwd)
            form_data.save()
            send_mail(
                'MobileApp Registration',
                msg,
                'abhishekabhi2333@gmail.com',
                [email_id],
                fail_silently=True

            )
            messages.success(request,'Registration Completed!!!')
            return redirect('home')
        else:
            messages.error(request,'Registration Failed')
            return render(request,"reg.html",{'form':form_data})      
        
class LoginView(FormView):
    form_class=LoginForm  
    template_name="login.html"
    def post(self,request):
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=uname,password=psw)
        if user:
            if user.usertype=="store":
                login(request,user)
                return redirect("str")
            login(request,user)
            return redirect("uhm")
        else:
            return redirect("login")

# class UserHome(TemplateView):
#     template_name="uhome.html" 
# 
# 
class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")           