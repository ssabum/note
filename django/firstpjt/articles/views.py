import random
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render 함수의 첫번째 인자는 반드시 request


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }
    return render(request, 'greeting.html', context)


def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    message = request.GET.get('message')
    # print(message)
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)

def dtl_practice(request):
    students = ['김지용', '박소현', '한승운', ' 임광훈', '주원상', '김보민']
    fruits = ['사과', ' 바나나', '포도', ' 감', '수박']
    user_list = []
    context = {
        'students': students,
        'fruits': fruits,
        'user_list': user_list,
    }

    return render(request, 'dtl_practice.html', context)
