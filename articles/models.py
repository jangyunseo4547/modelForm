from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # 수정되는 시간을 저장 
    updated_at = models.DateTimeField(auto_now = True) #현재 시간을 자동 저장

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE) # 외래키 : 부모 아이디 값이 저장되는 공간