from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider',)

admin.site.register(Image, ImageAdmin)