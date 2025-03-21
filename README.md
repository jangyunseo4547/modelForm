## 0,1 설정 동일

## modeling (`models.py`)
```python
class Article(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # 수정되는 시간을 자동 저장
    update_at = models.DateTimeField(auto_now = True) #현재 시간을 자동 저장
```

## migrate
`python manage.py makemigrations`
`python manage.py migrate`

## admin에 모델 추가 
```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

## 관리자 페이지 생성
`python manage.py createsuperuser`
`python manage.py runserver`
