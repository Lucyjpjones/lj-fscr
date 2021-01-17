from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_threads, name='forum'),
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
    path('add', views.add_thread, name='add_thread'),
    path('edit/<slug:slug>/', views.edit_thread, name='edit_thread'),
    path('delete/<slug:slug>/', views.delete_own_reply, name='delete_own_reply')
]
