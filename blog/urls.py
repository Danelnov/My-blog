from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('author/<str:author>/', views.author_posts, name="author_posts"),
    path('category/<str:category>', views.posts_by_category, name="posts_by_category")
]