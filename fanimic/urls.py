

from django.urls import path
from fanimic import views 

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('services/', views.Services, name='services'),
    path('contact', views.Contact, name='contact'),  
    path('fanimic/team/', views.Team, name='team'),  
    
    path('fanimic/building', views.Building, name='building'),  
    path('fanimic/electrical', views.Electrical, name='electrical'),  
    path('fanimic/decorator', views.Decorator, name='decorator'),  
    path('fanimic/projects', views.Project, name='project'),  
    path('fanimic/agriculture', views.Agriculture, name='agriculture'),  
    path('fanimic/manufacturing', views.Manufacturing, name='manufacturing'),       
]
