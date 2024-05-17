from django.shortcuts import render
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id') # Post 객체를 내림차순으로 모두 불러온 후에 posts 변수에 담음
    return render(request, 'list.html', {'posts' : posts}) # blog/index.html에서 posts 변수명으로 사용할 수 있도록!


