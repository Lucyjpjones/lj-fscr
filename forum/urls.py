from . import views
from django.urls import path


urlpatterns = [
    path('', views.forumPage, name='forum'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]
