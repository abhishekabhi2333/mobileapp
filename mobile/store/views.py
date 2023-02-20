from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import *
from user.models import User 
from .forms import StoreForm,AddproductForm
from django.contrib import messages
from .models import *

# Create your views here.
class StoreHome(CreateView):
    template_name="store.html"
    model=User
    form_class=StoreForm
    success_url=reverse_lazy("home")


class AddProducts(CreateView):
    template_name="addproducts.html"
    model=MobileModel
    form_class=StoreForm
    success_url=reverse_lazy('vpro')
# def post(self,request,*args,**kwargs):
#     form_data=self.form_class(request.POST)
#     if form_data.is_valid():
#         messages.success(request,"PRODUCT ADDEED!!!")
#         return redirect('vpro')
#     else:
#         messages.error(request,"FAILED")
#         return render(request,'addproducts.html',{'form':form_data})    


class ViewProduct(CreateView):
    def get(self,request):
        data=MobileModel.objects.all()
        return render(request,'viewproduct.html',{"data":data})


class ProductDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        eob=MobileModel.objects.get(id=id)
        eob.delete()
        return redirect('vpro')
           

class ProductEdit(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        item=MobileModel.objects.get(id=d_id)
        form=AddproductForm(instance=item)
        return render(request,"editproduct.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get('did')
        item=MobileModel.objects.get(id=d_id)
        form_data=AddproductForm(request.POST,files=request.FILES,instance=item)
        if form_data.is_valid():
            form_data.save()
            return redirect('vpro')
        else:
            return redirect('adpro')           