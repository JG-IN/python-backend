from django.conf.urls import url
from tweet import views

urlpatterns = [
    url(r'^api/tweet/(?P<user>.*)$', views.user)
]