from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('journey/', views.journey_index, name='index'),
    path('journey/<int:journey_id>/',views.journey_detail, name='detail'),
]