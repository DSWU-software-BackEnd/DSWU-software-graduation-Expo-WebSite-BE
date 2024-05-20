from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) # 제목 50자 제한
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)