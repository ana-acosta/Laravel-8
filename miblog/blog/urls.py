from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
                path('',views.PostListView.as_view(),name='PostListView'),
                path('<int:anho>/<int:mes>/<int:dia>/<slug:publicacion>/',
                        views.post_detalle, name='post_detalle'),
]