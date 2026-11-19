from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostForm, TagForm

def index(request):
	return render(request, 'blogs_django/index.html')

def tags(request):
	tags = Tag.objects.all()
	context = {'tags': tags}
	return render(request, 'blogs_django/tags.html', context)

def tag(request, tag_id):
	tag = Tag.objects.get(id=tag_id)
	posts = tag.posts.order_by('created_at')
	context = {'tag': tag, 'posts': posts}
	return render(request, 'blogs_django/tag.html', context)

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_django:tags')
    else:
        form = TagForm()
    return render(request, 'blogs_django/create_tag.html', {'form': form})

def posts(request):
	posts = Post.objects.all().order_by('created_at')
	context = {'posts': posts}
	return render(request, 'blogs_django/posts.html', context)

def post(request, post_id):
	post = Post.objects.get(id=post_id)
	context = {'post': post}
	return render(request, 'blogs_django/post.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('blogs_django:post', post.id)
    else:
        form = PostForm()
    return render(request, 'blogs_django/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs_django:post', post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post': post}
    return render(request, 'blogs_django/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blogs_django:posts')
    return redirect('blogs_django:post', post.id)