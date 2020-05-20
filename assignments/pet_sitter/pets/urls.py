from django.urls import path
from pets import views


urlpatterns = [
    path('', views.PetListView.as_view(), name='pets-list-page'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pets-details-page'),
    path('pets/create/', views.PetCreateView.as_view(), name='create'),
    path('pets/calendar/', views.CalendarListView.as_view(), name='calendar'),
]
