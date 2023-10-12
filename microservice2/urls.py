from django.urls import path
from . import views

urlpatterns = [
    path('endpoint2/', views.endpoint2, name='endpoint2'),
   
]
