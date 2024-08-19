from django.contrib import admin
from .models import Book, Genres, UserProfile

# Register your models here.

admin.site.register(Book)
admin.site.register(Genres)
admin.site.register(UserProfile)
