from django.contrib import admin
from .models import Track, Album, Genre, Like

# Register your models here.

admin.site.register([Track, Album, Genre, Like])