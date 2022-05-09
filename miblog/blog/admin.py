from django.contrib import admin
from.models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','slug','autor','fechapub','estado')
    list_filter = ('estado','creacion','fechapub','autor')
    search_fields = ('titulo','cuerpo')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'fechapub'
    ordering = ('estado','fechapub')
