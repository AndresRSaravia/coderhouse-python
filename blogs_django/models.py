from django.db import models
from django.contrib.auth.models import User

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
	# image = models.ImageField(upload_to='posts/', blank=True, null=True) no funciona pillow
	image = models.FileField(upload_to='posts/', blank=True, null=True)
	likes = models.PositiveIntegerField(default=0)
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	type = models.CharField(
		max_length=20,
		choices=POST_TYPES,
		default='borrador',
	)

	def __str__(self):
		return f"{self.title} - {self.author} ({self.created_at:%d/%m/%Y})"

