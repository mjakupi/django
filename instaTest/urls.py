
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PersonList.as_view()),
    url(r'^test/', views.index),

]

