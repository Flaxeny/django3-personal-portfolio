from django.shortcuts import render
from .models import BlogSpot


def all_blogs(request):
    blogs = BlogSpot.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
