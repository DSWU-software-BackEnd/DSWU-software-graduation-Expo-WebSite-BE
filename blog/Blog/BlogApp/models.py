from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title # 글 제목(title)으로 admin 페이지에서 목록을 확인하겠다