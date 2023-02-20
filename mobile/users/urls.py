from django.urls import path
from.views import *

urlpatterns=[
    path("uhme/",UserHome.as_view(),name="uhm")
]