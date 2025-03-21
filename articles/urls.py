from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name = 'index') # articles 생략
]
