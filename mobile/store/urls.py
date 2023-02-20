from django.urls import path
from .views import *


urlpatterns=[
    path('str/',StoreHome.as_view(),name='str'),
    path('adpro',AddProducts.as_view(),name='adpro'),
    path('vpro',ViewProduct.as_view(),name='vpro'),
    path('dltpro/<int:id>',ProductDelete.as_view(),name='dltpro'),
    path('editpro/<int:did>',ProductEdit.as_view(),name="editpro")
]