from django.shortcuts import render
from django.views.generic import*
from user.models import User
from .form import UserForm
from django.urls import reverse_lazy
from store.models import*
from store.forms import*
# Create your views here.
class UserHome(CreateView):
    template_name="uhome.html"
    model=MobileModel
    form_class=AddproductForm
    success_url=reverse_lazy("home")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        pro=self.model.objects.all() 
        context['data']=pro
        return context

class Addcart(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('pid')
        product=MobileModel.objects.get(id=pid)
        user=request.user
                