from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
