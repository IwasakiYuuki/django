from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^create/$', views.create_user, name='create_user'),
    url(r'^<int:question_id>/$', views.detail, name='detail'),
    url(r'^<int:question_id>/results$', views.results, name='result'),
    url(r'^<int:question_id>/vote$', views.vote, name='vote'),
]
