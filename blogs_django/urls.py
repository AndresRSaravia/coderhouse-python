from django.urls import path
from . import views

app_name = 'blogs_django'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('tags/', views.tags, name = 'tags'),
	path('tags/<int:tag_id>/', views.tag, name = 'tag'),
	path('tags/create/', views.create_tag, name='create_tag'),
	path('posts/', views.posts, name = 'posts'),
	path('posts/<int:post_id>/', views.post, name = 'post'),
	path('posts/create/', views.create_post, name='create_post'),
	path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
	path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]