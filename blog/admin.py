from django.contrib import admin
from .models import Post

@admin.register(Post) # igual a admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'created', 'updated')
  prepopulated_fields = { 'slug': ('title',)}
