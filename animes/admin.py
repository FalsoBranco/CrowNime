from django.contrib import admin

from .models import Anime, MediaTitle

# Register your models here.


@admin.register(MediaTitle)
class MediaTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    pass
