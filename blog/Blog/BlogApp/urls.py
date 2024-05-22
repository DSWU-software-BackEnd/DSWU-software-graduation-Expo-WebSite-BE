from django.urls import path
from .views import list, create, detail, update, delete # views.py의 함수 호출

urlpatterns = [
    path('', list, name = 'list'),
    path('create/', create, name = 'create'), # http://127.0.0.1:8000/create로 접속하면 views.py의 create 함수 실행
    path('detail/<int:id>', detail, name = "detail"), # http://127.0.0.1:8000/detail/게시물 id로 접속하면...
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]