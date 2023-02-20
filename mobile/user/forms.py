from django.contrib.auth.forms import UserCreationForm
from .models import User
from  django import forms

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name','last_name','email','username','password1','password2','phone','address','usertype'
        ]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120) 
    password=forms.CharField(max_length=120,widget=forms.PasswordInput)












# class Register(forms.Form):
#     name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}))
#     phonenumber=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your phone number","class":"form-control"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter your Email","class":"form-control"}))
#     password=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your password","class":"form-control"}))
#     repeatpassword=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your password","class":"form-control"}))
    
#     def clean(self):
#         cleaned_data=super().clean()
#         ph=cleaned_data.get("phone number")
#         cp=cleaned_data.get("password")
#         pw=cleaned_data.get("repeat password")
#         if len(ph)!=10:
#             msg=" Invalid phone number"
#             self.add_error('phonenumber',msg)
#         if cp!=pw:
#             msg="invalid password" 
#             self.add_error('repeatpassword',msg)

# class Login(forms.Form):
#     username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}))
#     password=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your phone number","class":"form-control"}))
   
