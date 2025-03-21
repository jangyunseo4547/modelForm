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

## Create 구현
- 1. articles앱 내에 (`forms.py`)
```python
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
   class Meta(): 
        model = Article
        fields = '__all__' # 모든 필드를 불러옴.
```
- 2. (`urls.py`)
```python

urlpatterns = [
    ...
    # Create
    path('create/', views.create, name = 'create'), 
    # 차이점 : 빈종이 보여주기 / 저장 한번에 처리
]
```
- 3. (`views.py`)
```python
def create(request):
    # new/ = 빈 종이를 보여주는 기능
    # create/ = 사용자가 입력한 데이터 저장
#===============================================
    # GET create/ = 빈 종이를 보여주는 기능
    # POST create/ = 사용자가 입력한 데이터 저장

    if request.method == 'POST':    # 2) create 이후
        form = ArticleForm(request.POST)  
        # title은 title, content는 content에 넣어서 form에서 알아서 넣어줌.
        
        if form.is_valid(): #데이터가 유효 -> 저장
            form.save()
            return redirect('articles:index') 

        else: # 데이터가 유효 x 경우 : 
            pass

    else:                            # 1) new 먼저 
        form = ArticleForm()
        context = {
            'form':form,
        }
        return render(request, 'create.html', context)
```

- 4. (`create.html`)
```python
{% extends 'base.html' %} # 공통 html 불러오기

{%  block body %}
    <form action="" method="POST"> # action에 비워두면 내 위치로 이동
        {% csrf_token %} 
        {{form}}
        <input type="submit">
    </form>
{% endblock %}
```
- modelform 결과 : required_id (꼭 넣어야 하는 정보) 생성
    - vaildation check : 사용자

