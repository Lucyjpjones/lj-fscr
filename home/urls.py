from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search_results', views.search_results, name='search_results'),
    path('meet_the_coaches', views.meet_the_coaches, name='meet_the_coaches'),
    path('about', views.about, name='about'),
    path('contact_us', views.contact_us, name='contact_us'),
]
