from django.contrib import admin
from .models import Post #models.py에서 정의한 모델을 import

admin.site.register(Post) #admin 사이트에서 해당 모델을 접근할 수 있게 됨

# Register your models here.
