from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # READ
    path('index/', views.index, name="index"),
    path('index/<int:pk>/', views.detail, name='detail'),

    # CREATE
    path('new/', views.new, name="new"),
    path('create/', views.create, name='create'),
    
    # DELETE
    path('index/<int:pk>/delete/', views.delete, name='delete'),

    # UPDATE
    path('index/<int:pk>/edit/', views.edit, name='edit'),
    path('index/<int:pk>/update', views.update, name='update'),
]
