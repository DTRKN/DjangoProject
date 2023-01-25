from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/results/', views.result, name='results'),
    path('<int:article_id>/vote/', views.vote, name='vote'),
]