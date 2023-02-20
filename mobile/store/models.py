from django.db import models
from user.models import User
# Create your models here.

class MobileModel(models.Model):
    image=models.ImageField(upload_to='blogimages',null=True)
    model=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    price=models.IntegerField()
    color=models.CharField(max_length=120,null=True)
    description=models.CharField(max_length=300)
    quantity=models.IntegerField(null=True)
    store=models.ForeignKey(User,on_delete=models.CASCADE,null=True)