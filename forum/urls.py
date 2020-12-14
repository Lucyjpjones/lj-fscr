from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_threads, name='forum'),
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
    path('add_thread', views.add_thread, name='add_thread'),
]
