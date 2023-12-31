from django.urls import path 
from . import views  #views.py에 있는 모든값들을 가져온다.

app_name = 'posts'   # app 이름

urlpatterns = [
    # Read
    path('',views.index, name='index'),
    path('<int:id>/', views.detail,name='detail'),
    # Create
    path('new/', views.new, name='new'), 
    path('create/',views.create, name='create'),
    path('<int:id>/delete/',views.delete, name='delete'),
    # update
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/',views.update, name='update'),

]