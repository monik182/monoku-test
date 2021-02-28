from django.contrib import admin
from .models import *


# Register your models here.
class SongAdmin(admin.ModelAdmin):
    fields = ('date', 'name', 'album', 'band', 'artist', 'length', 'genre', 'sub_genre', 'tags', 'instruments',
              'similar_bands')


class BandAdmin(admin.ModelAdmin):
    fields = ('name',)


class ArtistAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Song, SongAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Artist, ArtistAdmin)
