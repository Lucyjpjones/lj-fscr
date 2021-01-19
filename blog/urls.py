from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('delete/<slug:slug>/<int:comment_id>', views.delete_own_comment,
         name='delete_own_comment')
]
