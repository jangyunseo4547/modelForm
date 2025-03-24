from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    comments = article.comment_set.all()

    form = CommentForm()

    context = {
        'article':article,
        'form':form,
        'comments':comments,
    }
    return render(request, 'detail.html', context)

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

def update(request, id):
    article = Article.objects.get(id=id) # 업데이트할 게시글 아이디 찾기
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article) # 메소드가 POST일때 POST를 요청함.
        if form.is_valid(): # 데이터 유효하면 저장
            form.save()
            return redirect('articles:detail', id = id)

    else:
        form = ArticleForm(instance = article) # 메소드가 POST가 아닐경우 기존 게시글

    context = {
        'form':form,
    }
    return render(request, 'update.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False) # 바로 데이터베이스에 저장되지 않음.
        
            article = Article.objects.get(id=article_id)
            comment.article = article # 댓글이 해당 게시글과 연결되도록
            comment.save() # 데이터를 실제 저장 

            return redirect('articles:detail', id = article_id)

    else:
        return redirect('articles:index')

def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    
    return redirect('articles:detail', id=article_id)
    