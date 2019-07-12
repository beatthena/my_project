from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

#博客全
from App.models import User_tuijian,User,user_Blog,User_weivilla


def create1(request):
    username = request.session.get("username")
    userr = User.objects.filter(username=username).first()
    blog = user_Blog.objects.all()
    if request.method == "POST":
        print("*******************")
        pcontect = request.POST.get("pcontect")
        name_id= request.POST.get("name_id")
        res = user_Blog.objects.create(pcontect=pcontect,name_id=name_id)
        res.save()
    return render(request,"blog_post(full).html",context={
        'username': username,
        'session': request.session,
        'userr':userr,
        'blog':blog,

    })
# def create1(request):
#     if request.method == "POST":
#         pcontect = request.POST.get("pcontect")
#         res = user_Blog.objects.create(pcontect=pcontect)
#         res.save()
#     return

#博客左
def create2(request):
    username = request.session.get("username")
    userr = User.objects.filter(username=username).first()
    blog = user_Blog.objects.all()
    if request.method == "POST":
        print("*******************")
        pcontect = request.POST.get("pcontect")
        name_id= request.POST.get("name_id")
        res = user_Blog.objects.create(pcontect=pcontect,name_id=name_id)
        res.save()
    return render(request,"blog_post(left).html",context={
        'username': username,
        'session': request.session,
        'userr':userr,
        'blog':blog,

    })
#博客右
def create3(request):
    username = request.session.get("username")
    userr = User.objects.filter(username=username).first()
    blog = user_Blog.objects.all()
    if request.method == "POST":
        print("*******************")
        pcontect = request.POST.get("pcontect")
        name_id= request.POST.get("name_id")
        res = user_Blog.objects.create(pcontect=pcontect,name_id=name_id)
        res.save()
    return render(request,"blog_post(right).html",context={
        'username': username,
        'session': request.session,
        'userr':userr,
        'blog':blog,

    })


