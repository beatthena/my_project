"""lovelove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from App import views
#每个应用都有一个urls, 在这里将每个应用urls包含进来
# app/是应用的前缀,写什么请求路径就添加什么，views后面是没有东西的 例如 app/index2
urlpatterns = [
    url(r'^$', views.index,name='a'),#首页
    url(r'^(\d+)/$', views.index, name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),  #博客页面
    url(r'^change/$',views.change,name='change'),  #修改密码页面
    url(r'^change/(？P<username>\d+)$',views.change,name='change'),  #修改密码页面
    url(r'^contact/',views.contact),#联系人页面
    url(r'^faq/',views.faq),     #faq页面
    url(r'^properties/',include('properties.urls', namespace='properties')),  #属性页面
    url(r'^property/',include('property.urls', namespace='property')),#属性页
    url(r'^register/', views.register),  # 注册页面
    url(r'^login/', views.login,name="login"), # 登录页面
    url(r'^logout/', views.logout,name='logout'),# 退出页面
    url(r'^user/',include('user.urls', namespace='user')),

    url(r'^admin/', include('admin11.urls', namespace='admin')),

    url(r'^getcode/',views.getcode,name='getcode'),    #验证码


]
