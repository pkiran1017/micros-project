from django.urls import path
from . import views

urlpatterns = [
    path('endpoint1/', views.endpoint1, name='endpoint1'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
   
]
