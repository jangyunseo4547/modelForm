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

##
- `settings.py` 
```python
'DIRS': [BASE_DIR / 'templates'], # 밖에 있는 templates에 있는 파일도 탐지
```
- templates에 `base.html` 파일 생성
```shell
<body>
    <h1>여기는 base입니다.</h1>
    {% block body %}
    {% endblock %}
</body>
```

## Read 기능 구현
- 0. modelForm
```python
from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name = 'index') # articles 생략
]
```

- 1. articles 앱 내에 (`urls.py`)
```python
from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name = 'index') # articles 생략
]
```
- 2. articles 앱 내에 (`views.py`)
```python
def index(request):
    articles = Article.objects.all() # 전체 articles 찾기

    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)
```

- 3. articles 앱 안에 templates - `index.html`파일 생성
```
{% extends 'base.html' %}

{% block body %}
    {% for article in articles %}
        <h1>{{article.title}}</h1>
        <p>{{article.content}}</p>
    {% endfor %}
{% endblock %}
```