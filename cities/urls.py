
from django.conf.urls import url
from . import views

app_name = 'teams'

urlpatterns = [
    url(r'^$', views.TownsList.as_view()),

]