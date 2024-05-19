from django.shortcuts import render
from .models import Post

#어떻게 보여질 것인가..하하

def list(request):
    posts=Post.objects.all().order_by('-id') #post로 만든 객체 전부를 보여주는데 id 반대 정렬(최신순)으로 보여줘
    return render(request, 'list.html',{'post':posts})
        #화면을 렌더링 해주렴 그리고 해당 url에 있는걸 보여줘 여기서 post라는 변수 이름을 그대로 가져와서 사용할게

# Create your views here.
