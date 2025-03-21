from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }
    return render(request, 'index.html', context)

def create(request):
    # 모든 경우의 수 
        # - GET : form을 만들어서 html 문서를 사용자에게 마련
        # - POST : invalid data (데이터 검증 실패)
        # - post : valid data (데이터 검증 성공)

    # 5. POST 요청 (invalid data)
    # 10. POST 요청 (valid data)
    if request.method == 'POST':    
        # 6. 사용자가 입력한 데이터(request.POST)를 담은 form 생성 (invalid)
        # 11. 사용자가 입력한 데이터(request.POST)를 담은 form 생성 (valid)
        form = ArticleForm(request.POST)
        # 7. form 검증 실패
        # 12. form 검증 성공
        if form.is_valid(): #데이터가 유효 -> 저장
            # 13. form 저장
            form.save()
            # 14. index로 redirect
            return redirect('articles:index')

    # 1. GET 요청 : 비어있는 form(new) 만든다.
    else:                            
        form = ArticleForm()

    # 3. context dict에 비어있는 form을 담는다.
    # 8. context dict에 검증에 실패한 form을 담는다.
    context = {
        'form':form,
    }
    
    # 4. create.html을 랜더링
    # 9. create.html을 랜더링
    return render(request, 'create.html', context)