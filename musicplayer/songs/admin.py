from django.contrib import admin

# Register your models here.
from songs.models import Song


@admin.register(Song)
class Users(admin.ModelAdmin):
    pass
