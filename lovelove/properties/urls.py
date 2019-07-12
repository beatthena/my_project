from django.conf.urls import url

from properties import views


#属性路由
urlpatterns = [
    url(r'^$', views.properties, name='properties'),
    url(r'^(\d+)/$', views.properties, name='properties'),
    url(r'^properties2/$', views.properties2, name='properties2'),
    url(r'^properties2/(\d+)/$', views.properties2, name='properties2'),
    url(r'^properties3/$', views.properties3, name='properties3'),
    url(r'^properties3/(\d+)/$', views.properties3, name='properties3'),
]
