
from django.conf.urls import url,include
from . import views

app_name = 'teams'

urlpatterns = [
    url(r'^$', views.TeamList.as_view()),

]