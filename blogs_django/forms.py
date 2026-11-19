from django import forms
from .models import Post, Tag

INPUT_CLASSES = (
    'w-full px-3 py-2 bg-gray-950 border border-gray-700 rounded-lg '
    'text-gray-100 focus:outline-none focus:border-indigo-500'
)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': 'Nombre',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ej: Python, Django, Frontend...',
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'type', 'tags']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'type': 'Estado',
            'tags': 'Tags (puedes seleccionar varios)',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Título del post',
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 5,
                'placeholder': 'Escribe el contenido aquí...',
            }),
            'type': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': f'{INPUT_CLASSES} h-28',
            }),
        }