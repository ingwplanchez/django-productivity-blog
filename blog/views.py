# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

# Importamos login_required para proteger la vista en el futuro
from django.contrib.auth.decorators import login_required 

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Ahora la vista acepta el formulario de comentario
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all().order_by('-pub_date')

    form = CommentForm() # Inicializamos el formulario aquí

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # Usamos el usuario actual, si está logueado
            if request.user.is_authenticated:
                comment.author = request.user
                comment.save()
                return redirect('post_detail', post_id=post.id)
            else:
                # En un proyecto real, redirigiríamos al login
                # Por ahora, simplemente no guardamos el comentario
                # y podemos mostrar un mensaje de error
                # o redirigir a una página de error
                return render(request, 'blog/post_detail.html', {
                    'post': post,
                    'comments': comments,
                    'form': form,
                    'error_message': 'Debes iniciar sesión para comentar.'
                })

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})