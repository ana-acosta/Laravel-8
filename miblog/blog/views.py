
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

def post_detalle(request,anho,mes,dia,publicacion):
    post=get_object_or_404(Post,slug='publicacion',
                                estado='publicado',
                                fechapub_year=anho,
                                fechapub_month=mes,
                                fechapub_day= dia)
    return  render(request,'blog/post/detalle.html',
                   {'post':post})
class PostListView(ListView):
    queryset = Post.publicaciones.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/lista.html'