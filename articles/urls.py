from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name = 'index'), # articles 생략
    path('<int:id>/', views.detail, name= 'detail'),
    
    # Create
    path('create/', views.create, name = 'create'), # 빈종이 보여주기 / 저장 한번에 처리

    # update
    path('<int:id>/update/', views.update, name = 'update'), 

    # delete
    path('<int:id>/delete/', views.delete, name = 'delete'),

    # comment
    # create
    path('<int:article_id>/comments/create/', views.comment_create, name = 'comment_create'),

    # comment
    # delete
    path('<int:article_id>/comments/<int:id>/delete/', views.comment_delete, name = 'comment_delete'),

]
    