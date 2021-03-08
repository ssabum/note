from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 무조건 request
    context = {
        'name': '범희',
        'desc': '코딩..이렇게 쉬워도 될까?'
    }
    # render(reauest, template_name)
    # (1) request: render의 첫번째 인자도 반드시 request
    # (2) template_name: 'templates' 폴더에 위치한 템플릿 이름
    # (3) context: 템플릿과 함께 건네줄 데이터
    return render(request, 'index.html', context)

def detail(request, article_num):
    context = {
        'article_num': article_num,
    }
    return render(request, 'detail.html', context)