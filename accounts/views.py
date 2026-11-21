from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("blogs_django:posts")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect("blogs_django:posts")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)
    user_posts = request.user.posts.all()

    counts = {
        "total": user_posts.count(),
        "publicado": user_posts.filter(type="publicado").count(),
        "borrador": user_posts.filter(type="borrador").count(),
        "archivado": user_posts.filter(type="archivado").count(),
    }

    return render(request, "accounts/profile.html", {
        "profile": user_profile,
        "counts": counts,
    })

@login_required
def edit_profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Tu perfil fue actualizado correctamente.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=user_profile)

    return render(request, "accounts/edit_profile.html", {
        "u_form": u_form,
        "p_form": p_form,
    })
