from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from functools import wraps
from .models import Post, Tag
from .forms import PostForm, TagForm

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            messages.error(request, "Solo los administradores pueden gestionar etiquetas.")
            return redirect('blogs_django:tags')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def index(request):
    return render(request, 'blogs_django/index.html')

def search(request):
    query = request.GET.get('q', '').strip()
    posts = Post.objects.none()
    tags = Tag.objects.none()

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct().order_by('-created_at')

        tags = Tag.objects.filter(name__icontains=query).order_by('name')

    return render(request, 'blogs_django/search.html', {
        'query': query,
        'posts': posts,
        'tags': tags,
    })

# --- CRUD TAGS (Exclusivo Superusuarios) ---

def tags(request):
    query = request.GET.get('q', '').strip()
    tags = Tag.objects.all().order_by('name')
    if query:
        tags = tags.filter(name__icontains=query)
    return render(request, 'blogs_django/tags.html', {'tags': tags, 'query': query})

def tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.order_by('-created_at')
    return render(request, 'blogs_django/tag.html', {'tag': tag, 'posts': posts})

@superuser_required
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

@superuser_required
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

@superuser_required
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Etiqueta eliminada correctamente.")
        return redirect('blogs_django:tags')
    return redirect('blogs_django:tag', tag.id)

# --- CRUD POSTS ---

def posts(request):
    query = request.GET.get('q', '').strip()
    posts = Post.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blogs_django/posts.html', {'posts': posts, 'query': query})

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