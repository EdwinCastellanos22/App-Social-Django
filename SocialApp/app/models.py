from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='gato.jpg', upload_to='profile_images')
    bio = models.TextField(null=True, default='Biografia')

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    timestap= models.DateTimeField(default=timezone.now)
    content= models.TextField()

    class Meta:
        ordering= ['-timestap']

    def __str__(self):
        return f'{self.user.username}:{self.content}'