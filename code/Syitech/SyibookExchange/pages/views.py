from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView
#import operator
#from django.db.models import Q


# Create your views here.

def feed(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request, 'pages/newsfeed.html', context)

def user_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostForm()
    return render(request, 'pages/post.html', {'form' : form})


def success(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request, 'pages/newsfeed.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'pages/newsfeed.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
