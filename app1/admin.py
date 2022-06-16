from django.contrib import admin
from .models import library

# Register your models here.
class displaylibrary(admin.ModelAdmin):
    list_display = ('book_name','author_name','book_desc')

admin.site.register(library,displaylibrary)    
