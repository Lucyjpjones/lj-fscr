from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('meet_the_coaches', views.meet_the_coaches, name='meet_the_coaches'),
    path('about', views.about, name='about'),
]
