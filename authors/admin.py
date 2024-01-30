# в файле admin.py внутри приложения users

from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'born_date', 'born_location')
