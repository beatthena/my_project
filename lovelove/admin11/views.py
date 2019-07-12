import hashlib
from audioop import reverse
from itertools import count

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
# Create your views here.


# Create your views here.
from App.models import User, User_weivilla, User_tuijian, User_stylist, User_xiangqing, User_villalist


def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)  # 用户输入的姓名和密码
        print(9)
        password =hashlib.sha1(password.encode("utf8")).hexdigest()
        print(password)
        print(2)
        request.session["username"] = 'username'
        user = User.objects.filter(username=username, password=password)
        if user:
            return render(request, "admin/index1.html")
        else:
            return render(request, "admin/login1.html",{'msg': "用户名或密码错误"})
    return render(request,'admin/login1.html')


def index1(request):

    return render(request,'admin/index1.html')

# 推荐表的一切
def tuijian(request,page=1):
    bshu = User_tuijian.objects.all()
    geshu = User_tuijian.objects.count()
    print(user)
    print(1)
    # 一页五个
    paginator = Paginator(bshu, 5)
    print(paginator)
    print(4)
    # 创建分页对象
    page1 = int(page)
    print(page1)
    print(7)
    pagination = paginator.page(page1)
    print(pagination)
    print(5)
    if paginator.num_pages > 10:
        if page - 5 <= 0:
            customRange = range(1, 11)
        elif page + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(page - 5, page + 4)
    else:
        customRange = paginator.page_range
    print(customRange)
    print(6)
    return render(request, 'admin/tuijian.html', context={
        "dbss": pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count': geshu

    })

def newsType(request):
    return render(request,'admin/newsType.html')


def rote(request,page=1):
    bshu = User_weivilla.objects.all()
    geshu = User_weivilla.objects.count()
    print(user)
    print(1)
    # 一页五个
    paginator = Paginator(bshu, 9)
    print(paginator)
    print(4)
    # 创建分页对象
    page1 = int(page)
    print(page1)
    print(7)
    pagination = paginator.page(page1)
    print(pagination)
    print(5)
    if paginator.num_pages > 10:
        if int(page) - 5 <= 0:
            customRange = range(1, 11)
        elif int(page) + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(int(page) - 5, int(page) + 4)
    else:
        customRange = paginator.page_range
    print(customRange)
    print(6)
    return render(request, 'admin/rote.html', context={
        "dbss": pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count' : geshu

    })


def user(request,page=1):
    # 用户
    user = User.objects.all()
    print(user)
    print(1)
    geshu = User.objects.count()
    #一页五个
    paginator = Paginator(user, 5)
    print(paginator)
    print(4)
    # 创建分页对象
    page1 = int(page)
    print(page1)
    print(7)
    pagination = paginator.page(page1)
    print(pagination)
    print(5)
    if paginator.num_pages > 10:
        if page - 5 <= 0:
            customRange = range(1, 11)
        elif page + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(page - 5, page + 4)
    else:
        customRange = paginator.page_range
    print(customRange)
    print(6)
    return render(request, 'admin/user.html', context={
        "dbss":pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count': geshu
    })


#后端修改密码页面
def updatePwd(request):
    username = request.session.get("username")

    if request.method == "POST":

        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('recpassword')

        print(pwd1, pwd2)
        print("++++++++")
        if pwd1 != pwd2:
            return render(request, "change-password.html", {'msg': "密码输入不一致"})
        else:
            pwd1 = hashlib.sha1(pwd1.encode("utf8")).hexdigest()
            u1 = User.objects.get(username=username)
            u1.password = pwd1
            u1.save()
            return redirect(reverse('login'))

    return render(request, 'admin/updetePwd.html', context={
        'session': request.session,
        'username': username

    })








def news(request):
    return render(request, 'admin/news.html')
def cuiwu(request):
    return render(request,'admin/4041.html')

# 用户增加
def create(request):
    if request.method=='POST':
        # uid =request.POST.get("uid")
        username =request.POST.get("username")
        password =request.POST.get("password")
        password1 = hashlib.sha1(password.encode("utf8")).hexdigest()
        usertype = request.POST.get("usertype")
        res = User.objects.create(username=username,password=password1,usertype=usertype)
        res.save()
    return render(request,'admin/create.html')
#用户删除
def delete(request,id=1):
    if request.method == 'POST':
        print(id)
        print(15)
        uid = User.objects.get(pk=id)
        uid.delete()
        # res = User.objects.delete(id = uid)
        # res.save()
    return render(request,'admin/delete.html')
#用户的修改
def update3(request,id=1):
    uid = User.objects.get(pk=id)
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        type = request.POST.get("type")
        uid.username = username
        uid.password =password
        uid.type=type
        uid.save()
    return render(request,'admin/update3.html',context={
        'uid':uid,
    })
#别墅增加
def create1(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        money = request.POST.get("money")
        area = request.POST.get("area")
        weivilla_photo = request.POST.get("weivilla_photo")
        id = request.POST.get("id")
        res = User_weivilla.objects.create(name=name,money=money,area=area,weivilla_photo=weivilla_photo,id=id)
        print(res)
        print(55)
        res.save()
    return render(request, 'admin/create1.html')

#别墅删除
def delete1(request,id=1):
    if request.method == 'POST':
        print(id)
        uid = User_weivilla.objects.get(pk=id)
        uid.delete()
    return render(request,'admin/delete1.html')
#别墅修改
def update(request,id=1):
    uid = User_weivilla.objects.get(pk=id)
    if request.method =='POST':
        name = request.POST.get("name")
        money = request.POST.get("money")
        area = request.POST.get("area")
        weivilla_photo = request.POST.get("weivilla_photo")
        uid.name = name
        uid.money =money
        uid.area = area
        uid.weivilla_photo=weivilla_photo
        uid.save()
    return render(request,'admin/update.html',context={
        'uid':uid,
    })

#推荐表增加
def create2(request):
    if request.method == 'POST':
        #id = request.POST.get("id")
        name = request.POST.get("name")
        money = request.POST.get("money")
        tuijian_photo = request.POST.get("tuijian_photo")
        res = User_tuijian.objects.create(name=name,money=money,tuijian_photo=tuijian_photo)
        print(res)
        print(55)
        res.save()
    return render(request, 'admin/create2.html')

# 推荐表的删除
def delete2(request,id=1):
    if request.method == 'POST':
        print(id)
        uid = User_tuijian.objects.get(pk=id)
        uid.delete()
    return render(request,'admin/delete2.html')
# 推荐表的修改
def update1(request,id=1):
    uid = User_tuijian.objects.get(pk=id)
    if request.method =='POST':
        name = request.POST.get("name")
        money = request.POST.get("money")
        tuijian_photo = request.POST.get("tuijian_photo")
        uid.name = name
        uid.money =money
        tuijian_photo=tuijian_photo
        uid.save()
    return render(request,'admin/update1.html',context={
        'uid':uid,
    })








# 设计师表
def shejishi(request,page=1):
    bshu = User_stylist.objects.all()
    geshu = User_stylist.objects.count()

    # 一页五个
    paginator = Paginator(bshu, 5)

    # 创建分页对象
    page1 = int(page)

    pagination = paginator.page(page1)

    if paginator.num_pages > 10:
        if int(page) - 5 <= 0:
            customRange = range(1, 11)
        elif int(page) + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(int(page) - 5, int(page) + 4)
    else:
        customRange = paginator.page_range

    return render(request, 'admin/shejishi.html', context={
        "dbss": pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count': geshu

    })

# 设计师的增加
def create3(request):
    if request.method == 'POST':
        #id = request.POST.get("id")
        sname = request.POST.get("sname")
        stype = request.POST.get("stype")
        signature = request.POST.get("signature")
        res = User_stylist.objects.create(signature=signature,stype=stype,sname=sname)
        print(res)
        print(55)
        res.save()
    return render(request, 'admin/create3.html')
# 设计师的删除
def delete3(request,id=1):
    if request.method == 'POST':
        print(id)
        uid = User_stylist.objects.get(pk=id)
        uid.delete()
    return render(request,'admin/delete3.html')
# 设计师的修改
def update2(request,id=1):
    uid = User_stylist.objects.get(pk=id)
    if request.method =='POST':
        sname = request.POST.get("sname")
        stype = request.POST.get("stype")
        signature = request.POST.get("signature")
        uid.name = sname
        uid.stype =stype
        uid.signature=signature
        uid.save()
    return render(request,'admin/update2.html',context={
        'uid':uid,
    })


def xiangqing(request,page=1):
    bshu = User_xiangqing.objects.all()
    geshu = User_xiangqing.objects.count()

    # 一页五个
    paginator = Paginator(bshu, 5)

    # 创建分页对象
    page1 = int(page)

    pagination = paginator.page(page1)

    if paginator.num_pages > 10:
        if int(page) - 5 <= 0:
            customRange = range(1, 11)
        elif int(page) + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(int(page) - 5, int(page) + 4)
    else:
        customRange = paginator.page_range

    return render(request, 'admin/xiangqing.html', context={
        "dbss": pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count': geshu
    })


def create4(request):
    if request.method == 'POST':
        # id = request.POST.get("id")
        id = request.POST.get("id")
        name = request.POST.get("name")
        money = request.POST.get("money")
        miaoshu = request.POST.get("miaoshu")
        res = User_xiangqing.objects.create(id=id,name=name,money=money,miaoshu=miaoshu)
        print(res)
        print(55)
        res.save()
    return render(request, 'admin/create4.html')


def delete4(request,id=1):
    if request.method == 'POST':
        print(id)
        uid = User_xiangqing.objects.get(pk=id)
        uid.delete()
    return render(request, 'admin/delete4.html')


def update4(request,id=1):
    uid = User_xiangqing.objects.get(pk=id)
    if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get("name")
        money = request.POST.get("money")
        miaoshu = request.POST.get("miaoshu")
        uid.id = id
        uid.name=name
        uid.money=money
        uid.miaoshu=miaoshu
        uid.save()
    return render(request, 'admin/update4.html', context={
        'uid': uid,
    })


def yangshi(request,page=1):
    bshu = User_villalist.objects.all()
    geshu = User_villalist.objects.count()

    # 一页五个
    paginator = Paginator(bshu, 5)

    # 创建分页对象
    page1 = int(page)

    pagination = paginator.page(page1)

    if paginator.num_pages > 10:
        if int(page) - 5 <= 0:
            customRange = range(1, 11)
        elif int(page) + 4 > paginator.num_pages:
            customRange = range(paginator.num_pages - 9, paginator.num_pages + 1)
        else:
            customRange = range(int(page) - 5, int(page) + 4)
    else:
        customRange = paginator.page_range

    return render(request, 'admin/yangshi.html', context={
        "dbss": pagination.object_list,
        'pagerange': customRange,
        'pagination': pagination,
        'paginator': paginator,
        'count': geshu
    })


def create5(request):
    if request.method == 'POST':

        bedroom = request.POST.get("bedroom")
        garage = request.POST.get("garage")
        bathroom = request.POST.get("bathroom")
        washhouse = request.POST.get("washhouse")
        swimming = request.POST.get("swimming")
        lawn = request.POST.get("lawn")
        bikeway=request.POST.get("bikeway")
        res = User_villalist.objects.create(bikeway=bikeway,swimming=swimming,lawn=lawn,washhouse=washhouse,bedroom=bedroom,garage=garage,bathroom=bathroom)
        print(res)
        print(55)
        res.save()
    return render(request, 'admin/create5.html')


def delete5(request, id=1):
    if request.method == 'POST':
        print(id)
        uid = User_villalist.objects.get(pk=id)
        uid.delete()
    return render(request, 'admin/delete5.html')


def update5(request, id=1):
    uid = User_villalist.objects.get(pk=id)
    if request.method == 'POST':
        bedroom = request.POST.get("bedroom")
        garage = request.POST.get("garage")
        bathroom = request.POST.get("bathroom")
        washhouse = request.POST.get("washhouse")
        swimming = request.POST.get("swimming")
        lawn = request.POST.get("lawn")
        bikeway = request.POST.get("bikeway")
        uid.washhouse=washhouse
        uid.swimming=swimming
        uid.lawn =lawn
        uid.bikeway=bikeway
        uid.bedroom = bedroom
        uid.garage = garage
        uid.bathroom = bathroom
        uid.save()
    return render(request, 'admin/update5.html', context={
        'uid': uid,
    })