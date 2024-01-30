# users/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Author
from .utils import get_postgresql

# Create your views here.


def main(request, author_id):
    try:
        author = get_object_or_404(Author, id=author_id)

        return render(request, "users/index.html", context={'users': [author]})
    except Exception as e:
        return HttpResponse(f"Invalid author ID format: {e}")


def author_list(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'users/users.html', context={'author': author})
