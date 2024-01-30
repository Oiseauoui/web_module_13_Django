# quotes/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = "quotes"

urlpatterns = [


    path("", views.main, name="root"),
    path('<int:page>/', views.main, name="root_paginate"),
    path('add_author/', views.add_author, name='add_author'),
    path('author_list/', views.author_list, name='author_list'),
    path('author/<int:author_id>/', views.author_list, name='author_list'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quotes/', views.main, name='quotes'),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('top-tags/', views.top_tags, name='top_tags'),


]
