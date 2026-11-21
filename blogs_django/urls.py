from django.urls import path
from . import views

app_name = 'blogs_django'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # CRUD Tags
    path('tags/', views.tags, name='tags'),
    path('tags/<int:tag_id>/', views.tag, name='tag'),
    path('tags/create/', views.create_tag, name='create_tag'),
    path('tags/<int:tag_id>/edit/', views.edit_tag, name='edit_tag'),
    path('tags/<int:tag_id>/delete/', views.delete_tag, name='delete_tag'),
    # CRUD Posts
    path('posts/', views.posts, name='posts'),
	path('posts/my_posts/', views.my_posts, name='my_posts'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]