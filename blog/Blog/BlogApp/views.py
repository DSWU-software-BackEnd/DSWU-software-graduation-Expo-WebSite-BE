from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id') # Post 객체를 내림차순으로 모두 불러온 후에 posts 변수에 담음
    return render(request, 'BlogApp/list.html', {'posts' : posts}) # blog/index.html에서 posts 변수명으로 사용할 수 있도록!

# CRUD
def create(request):
    if request.method == 'POST': # 사용자의 요청이 POST라면
        title = request.POST.get('title') # 사용자가 입력한 title, content 데이터에서 'title', 'content' 값 추출
        content = request.POST.get('content')

        post = Post.objects.create( # 새로운 Post 데이터를 생성하고 데이터베이스에 저장 (추출한 title과 content를 DB의 title, content 필드에 할당)
            title = title,
            content = content,
        )
        return redirect('list') # 글 생성 후 사용자를 글 목록 페이지로 이동시킴 (path의 name 작성)
    return render(request, 'BlogApp/create.html') # 사용자의 요청이 POST가 아닌 경우 (http://127.0.0.1:8000/create 페이지에 GET으로 접속할 때)

def detail(request, id):
    post = get_object_or_404(Post, id = id) # 사용자가 요청한 id를 가진 Post 데이터를 DB에서 찾음, django가 찾아야 할 데이터의 id와 사용자가 요청한 id 값이 같은지 확인
    return render(request, 'BlogApp/detail.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save() # post 데이터의 변경 사항을 데이터베이스에 저장
        return redirect('detail', id)
    return render(request, 'BlogApp/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete() # 데이터를 찾으면 데이터베이스에서 삭제
    return redirect('list')