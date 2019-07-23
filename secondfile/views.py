from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
import random

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def create(request):
    post = Post()
    post.title = request.POST['post_title']
    post.body = request.POST['post_body']
    post.pub_date = timezone.now()
    if request.FILES:
        post.image = request.FILES['image']
    post.save()

    return redirect('home')

def detail(request,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def read(request):
    posts = Post.objects.all()
    return render(request, 'read.html', {"posts":posts})

def front(request):
    return render(request, 'front.html')

def update(request, post_id):
    updated_post = get_object_or_404(Post, pk=post_id)
    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    updated_post.save()
    return redirect('/post/' + str(update_post.id))

def renew(request, post_id):
    renew_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'renew.html', {'renew' : renew_post})

def delete(request, post_id):
    delete_post = get_object_or_404(Post, pk=post_id)
    delete_post.delete()
    return redirect('home')