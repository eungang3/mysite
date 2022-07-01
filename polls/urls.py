from django.urls import path 
from . import views 

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail', views.question, name='question'),
    path('<int:id>/vote', views.vote, name="vote"),
    path('<int:id>/results', views.results, name='results')
]