from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# READ
def index(request):
    # 모든 게시글 조회
    # articles = Article.objects.all()[::-1] # 파이썬 언어로 해결
    articles = Article.objects.order_by('-updated_at') # DB 단에서 해결, 수정순으로 정렬
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# CREATE
def new(request):
    return render(request, 'articles/new.html')

# CREATE
def create(request):
    # POST 요청으로 들어온 사용자 데이터를 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Article 모델 클래스를 기반으로 인스턴스를 생성
    article = Article(title=title, content=content)

    # DB에 저장
    article.save()

    # return render(request, 'articles/index.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# READ
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# DELETE
# 발동조건: /articles/index/게시글번호/delete
# 띠라서 POST만 삭제되게 만들어야 한다
def delete(request, pk):
    # 삭제할 데이터 불러오기
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 삭제
        article.delete()
        # 메인페이지로 이동
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

# UPDATE
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)
def update(request, pk):
    # 수정할 게시글 불러오기
    article = Article.objects.get(pk=pk)
    
    # 사용자가 건네준 데이터 추출
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    # DB에 저장
    article.save()

    return redirect('articles:detail', article.pk)

