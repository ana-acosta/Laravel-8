from logging import Manager
from django.db import models
from django.utils import  timezone
from django.urls import  reverse
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado='publicado')

class PostManager2(models.Manager):
    def get_queryset(self):
        return  super().get_queryset().filter(estado='borrador')

class Post(models.Model):
    STATUS_CHOICES = {
        ('borrador','Borrador'),
        ('publicado', 'Publicado'),
    }
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='fechapub')
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='entradas_blog')
    cuerpo = models.TextField()
    fechapub = models.DateTimeField(default=timezone.now)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='borrador')
    objectos = models.manager()
    publicaciones = PostManager()
    borradores = PostManager2()

    class Meta:
        ordering = ('-fechapub',)

    def __str__(self):
        return (self.titulo)

    def get_absolute_url(self):
        return reverse('blog:post_detalle' ,
                       args=[self.fechapub.year,
                             self.fechapub.month,
                             self.fechapub.day,self.slug])


