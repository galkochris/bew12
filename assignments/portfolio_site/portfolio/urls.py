from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('greet/<str:name>/', views.greet_by_name),
]