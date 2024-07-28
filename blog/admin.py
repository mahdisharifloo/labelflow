from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.BlogCard)
class BlogCardAdmin(admin.ModelAdmin):
    pass 