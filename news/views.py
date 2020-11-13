from django.shortcuts import render

from django.http import HttpResponse

from django.urls import path, include


def post_list(request):
    return render(request, 'news/post_list.html', {})
