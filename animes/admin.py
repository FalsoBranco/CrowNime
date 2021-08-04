from django.contrib import admin

from .models import Anime, Genre, MediaTitle

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(MediaTitle)
class MediaTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    pass
