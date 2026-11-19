from django.db import models
from django.contrib.auth.models import User # Recomendado para el campo author
from django.conf import settings

class Tag(models.Model):
	"""Representa una etiqueta para categorizar los posts."""
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	POST_TYPES = [
		("borrador", "Borrador"),
		("publicado", "Publicado"),
		("archivado", "Archivado"),
	]
	"""Representa un posteo o entrada dentro de la plataforma."""
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	tags = models.ManyToManyField(Tag, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	# Opciones para el campo 'type' (estado del post)
	type = models.CharField(
		max_length=20,
		choices=POST_TYPES,
		default='borrador',
	)
	def __str__(self):
		return f"{self.title} - {self.author} ({self.created_at})"

