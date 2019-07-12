from django.conf.urls import url

from blog import views


#常见问题页面路由
urlpatterns = [
url(r'^blog_post_full/$', views.create1, name='blog_post_full'),
url(r'^blog_post_left/$', views.create2, name='blog_post_left'),
url(r'^blog_post_right/$', views.create3, name='blog_post_right'),
    ]
