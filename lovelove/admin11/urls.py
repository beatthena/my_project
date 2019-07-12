from django.conf.urls import url

from admin11 import views

urlpatterns = [


    url(r'^index1/',views.index1,name='index1'),
    url(r'^login1/', views.login1, name='login1'),
    url(r'^newsType/',views.newsType,name='newsType'),
    url(r'^rote/$',views.rote,name='rote'),
    url(r'^rote/(?P<page>\d+)/$',views.rote,name='rote'),
    url(r'^user/$', views.user, name='user'),
    url(r'^user/(?P<page>\d+)/$', views.user, name='user'),
    url(r'^tuijian/$', views.tuijian, name='tuijian'),
    url(r'^tuijian/(?P<page>\d+)/$', views.tuijian, name='tuijian'),
    url(r'^updatePwd',views.updatePwd,name='updatePwd'),
    url(r'^news',views.news,name='news'),
    url(r'^cuiwu',views.cuiwu,name='cuiwu'),
    url(r'^shejishi/$', views.shejishi, name='shejishi'),
    url(r'^shejishi/(?P<page>\d+)/$', views.shejishi, name='shejishi'),

    #用户的增删改查
    url(r'^create/$',views.create,name='create'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    url(r'^update3/$', views.update3, name='update3'),
    url(r'^update3/(?P<id>\d+) /$', views.update3, name='update3'),
    # 别墅的增删改查
    url(r'^create1/$', views.create1, name='create1'),
    url(r'^delete1/$', views.delete1, name='delete1'),
    url(r'^delete1/(?P<id>\d+)/$', views.delete1, name='delete1'),
    url(r'^update/$',views.update,name='update'),
    url(r'^update/(?P<id>\d+)/$',views.update,name='update'),

    # 推荐表的增删改查
    url(r'^create2/$', views.create2, name='create2'),
    url(r'^create2/(?P<id>\d+)/$', views.create2, name='create2'),
    url(r'^delete2/$', views.delete2, name='delete2'),
    url(r'^delete2/(?P<id>\d+)/$', views.delete2, name='delete2'),
    url(r'^update1/$',views.update1,name='update1'),
    url(r'^update1/(?P<id>\d+)/$',views.update1,name='update1'),

    #设计师的增删改查
    url(r'^create3/$', views.create3, name='create3'),
    url(r'^create3/(?P<id>\d+)/$', views.create3, name='create3'),
    url(r'^delete3/$', views.delete3, name='delete3'),
    url(r'^delete3/(?P<id>\d+)/$', views.delete3, name='delete3'),
    url(r'^update2/$',views.update2,name='update2'),
    url(r'^update2/(?P<id>\d+)/$',views.update2,name='update2'),


    #详情的增删改查
    url(r'^xiangqing/$', views.xiangqing, name='xiangqing'),
    url(r'^xiangqing/(?P<page>\d+)/$', views.xiangqing, name='xiangqing'),

    url(r'^create4/$', views.create4, name='create4'),
    url(r'^create4/(?P<id>\d+)/$', views.create4, name='create4'),
    url(r'^delete4/$', views.delete4, name='delete4'),
    url(r'^delete4/(?P<id>\d+)/$', views.delete4, name='delete4'),
    url(r'^update4/$',views.update4,name='update4'),
    url(r'^update4/(?P<id>\d+)/$',views.update4,name='update4'),

    #样式的增删改查
    url(r'^yangshi/$', views.yangshi, name='yangshi'),
    url(r'^yangshi/(?P<page>\d+)/$', views.yangshi, name='yangshi'),

    url(r'^create5/$', views.create5, name='create5'),
    url(r'^create5/(?P<id>\d+)/$', views.create5, name='create5'),
    url(r'^delete5/$', views.delete5, name='delete5'),
    url(r'^delete5/(?P<id>\d+)/$', views.delete5, name='delete5'),
    url(r'^update5/$',views.update5,name='update5'),
    url(r'^update5/(?P<id>\d+)/$',views.update5,name='update5'),




]