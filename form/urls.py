from django.contrib import admin
from django.urls import path,include
from form import views
from form.views import index
app_name='form'
urlpatterns = [
    path('index', views.index, name = 'index'),
    path('info', views.info, name = 'info'),
    path('event', views.event, name = 'event'),
    path('contactus', views.contactus, name = 'contactus'),
    path('register',views.register,name='register'),
]