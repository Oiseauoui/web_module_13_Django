# quotes/views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm
from django.db.models import Count



def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10

    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('quotes:root')
    else:
        author_form = AuthorForm()

    return render(request, 'users/add_author.html', context={'author_form': author_form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            return redirect('quotes:root')
    else:
        quote_form = QuoteForm()

    return render(request, 'quotes/add_quote.html', context={'quote_form': quote_form})


def author_list(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'users/users.html', context={'author': author})


def quotes_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    authors = Author.objects.filter(quote__in=quotes).distinct()
    return render(request, 'quotes/quotes_by_tag.html', {'quotes': quotes, 'users': authors})


def top_tags(request):
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    return render(request, 'quotes/top_tags.html', {'top_tags': top_tags})
