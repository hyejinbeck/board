from django.urls import path 
from . import views  #views.py에 있는 모든값들을 가져온다.

app_name = 'posts'   # app 이름

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/', views.detail,name='detail'),

]