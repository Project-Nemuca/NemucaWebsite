from django.conf.urls import url

from . import views

app_name = 'acumen'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]