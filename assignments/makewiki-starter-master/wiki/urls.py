from django.urls import path
from wiki import views


urlpatterns = [
    path('', views.PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', views.PageDetailView.as_view(), name='wiki-details-page'),
    path('wiki/create/', views.PageCreateView.as_view(), name='create'),
]
