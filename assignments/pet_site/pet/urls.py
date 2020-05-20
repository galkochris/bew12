  
from django.urls import path
from django.contrib import admin
from . import views
from pet.views import HomeView, PetCreateView, PetListView, PetDetailView, AppointmentCreateView, CalendarListView, SignUpView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('pets/',PetListView.as_view(), name="pet-list-page"),
    path('pet/create/', views.PetCreateView.as_view(), name='pet-create-page'), 
    path('pets/<int:pet_id>/', PetDetailView.as_view(), name="pet-detail-page"),
    path('calendar/', CalendarListView.as_view(), name='calendar-list-page'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment-create-page'),
    path('signup/', SignUpView.as_view(), name='sign-up'),
]