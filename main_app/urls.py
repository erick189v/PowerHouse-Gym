from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('demo/', views.demo, name='demo'),
    path('about/', views.about, name='about'),
    path('journeys/', views.journey_index, name='index'),
    path('journeys/<int:journey_id>/',views.journeys_detail, name='detail'),
    path('journeys/create/', views.JourneyCreate.as_view(), name='journeys_create'),
    path('journeys/<int:pk>/update/', views.JourneyUpdate.as_view(), name='journeys_update'),
    path('journeys/<int:pk>/delete/', views.JourneyDelete.as_view(), name='journeys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]