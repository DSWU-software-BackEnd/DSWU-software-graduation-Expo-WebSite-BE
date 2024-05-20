from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id') #Post 객체를 내림차순으로 모두 불러온 후에 posts 변수에 담음
    return render(request, 'list.html', {'posts': posts}) #blog/ index.html에서 posts 변수명으로 사용할 수 있도록!


#CRUD
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title= title,
            content = content,
        )
        return redirect('list')
    return render(request, 'create.html')

def detail(request, id):
    post = get_object_or_404(Post, id =id)
    return render(request, 'detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('list')