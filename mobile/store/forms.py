from django import forms
from user.models import User
from.models import MobileModel

class StoreForm(forms.ModelForm):
    class Meta:
        model=MobileModel
        fields="__all__"

        
class AddproductForm(forms.ModelForm):
    class Meta:
        model=MobileModel
        fields="__all__"        