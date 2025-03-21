from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name = 'index'), # articles 생략
    
    # Create
    path('create/', views.create, name = 'create'), # 빈종이 보여주기 / 저장 한번에 처리
]
