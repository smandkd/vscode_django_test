from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>', views.photo_detail, name='photo_detail'),
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
]
# path 의 매개변수 
# '' : "https://127.0.0.1:8000"
# views.photo_list : views.py 의 photo_list 함수를 부른다.
# 깃 커밋
# 깃 커밋2