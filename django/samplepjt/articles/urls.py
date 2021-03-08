from django.urls import path
from . import views

# 'articles/'
urlpatterns = [
    # 'articles/index/'로 요청했을 경우 뷰 함수의 index 수행
    path('index/', views.index),
    # 'articles/1/'로 요쳥했을 경우 뷰 함수의 detail 수행
    path('<int:article_num>/', views.detail),
]