from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Tag
from .forms import PostForm, TagForm

def index(request):
    return render(request, 'blogs_django/index.html')

# --- CRUD TAGS ---

def tags(request):
    tags = Tag.objects.all().order_by('name')
    return render(request, 'blogs_django/tags.html', {'tags': tags})


def tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.order_by('-created_at')
    return render(request, 'blogs_django/tag.html', {'tag': tag, 'posts': posts})

@login_required
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Etiqueta creada correctamente.")
            return redirect('blogs_django:tags')
    else:
        form = TagForm()
    return render(request, 'blogs_django/create_tag.html', {'form': form})

@login_required
def edit_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Etiqueta actualizada correctamente.")
            return redirect('blogs_django:tag', tag.id)
    else:
        form = TagForm(instance=tag)
    return render(request, 'blogs_django/edit_tag.html', {'form': form, 'tag': tag})

@login_required
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Etiqueta eliminada correctamente.")
        return redirect('blogs_django:tags')
    return redirect('blogs_django:tag', tag.id)

# --- CRUD POSTS ---

def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogs_django/posts.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogs_django/post.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post creado correctamente.")
            return redirect('blogs_django:post', post.id)
    else:
        form = PostForm()
    return render(request, 'blogs_django/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "No tienes permiso para editar este post.")
        return redirect('blogs_django:post', post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente.")
            return redirect('blogs_django:post', post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs_django/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "No tienes permiso para eliminar este post.")
        return redirect('blogs_django:post', post.id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post eliminado correctamente.")
        return redirect('blogs_django:posts')
    return redirect('blogs_django:post', post.id)