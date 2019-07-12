from django.conf.urls import url

from property import views

#属性路由
urlpatterns = [
    url(r'^$', views.property, name='property'),
    url(r'^property/(?P<id>\d+)$', views.property, name='property'),
    url(r'^property2/$', views.property2, name='property2'),
    url(r'^property2/(?P<id>\d+)$', views.property2, name='property2'),
    url(r'^property3/$', views.property3, name='property3'),
    url(r'^property3/(?P<id>\d+)/$', views.property3, name='property3'),

]