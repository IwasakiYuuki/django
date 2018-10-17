from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url('', views.index, name='index'),
#    url('create/', views.create_user, name='create_user'),
    url('<int:question_id>/', views.detail, name='detail'),
    url('<int:question_id>/results', views.results, name='result'),
    url('<int:question_id>/vote', views.vote, name='vote'),
]
