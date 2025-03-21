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
    # new/ = 빈 종이를 보여주는 기능
    # create/ = 사용자가 입력한 데이터 저장
#===============================================
    # GET create/ = 빈 종이를 보여주는 기능
    # POST create/ = 사용자가 입력한 데이터 저장

    if request.method == 'POST':    # create 이후
        form = ArticleForm(request.POST)  # title은 title, content는 content에 넣어서 form으로 묶어줌.
        
        if form.is_valid(): #데이터가 유효 -> 저장
            form.save()
            return redirect('articles:index')

        else: #데이터가 유효 x 경우 : 
            context = {
                'form':form,
            }
            return render(request, 'create.html', context)

    else:                            # new 먼저 
        form = ArticleForm()
        context = {
            'form':form,
        }
        return render(request, 'create.html', context)