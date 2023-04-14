from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'netstatus',)

admin.site.register(Image, ImageAdmin)