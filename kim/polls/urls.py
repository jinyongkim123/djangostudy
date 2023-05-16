from django.urls import path #path 임포트트

from . import views

urlpatterns = [ #모든 urls은 파일은 라우팅 인포메이션
    path('', views.index, name='index'),
     #ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/5/results/
    path('<int:question_id>/result/',views.results, name='results'),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]