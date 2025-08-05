# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all().order_by('-pub_date') # Obtiene los comentarios del post
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})