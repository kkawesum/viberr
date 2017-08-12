from django.contrib import admin
from .models import Album,Song

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist','album_title','genre')

admin.site.register(Album,AlbumAdmin)

admin.site.register(Song)

# Register your models here.
