import hashlib
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, HttpResponseRedirect
from django.urls import reverse

from App.forms import UserForm
from App.models import User, User_weivilla, User_villalist, User_tuijian, User_stylist, user_Blog
# Create your views here.

# 首页1
from App.utils import get_color, generate_code
from lovelove import settings


def index(request,id=1):
    dbs = User_weivilla.objects.all()[0:7:1]
    beishu1 = User_weivilla.objects.get(pk=id)

    username = request.session.get("username")

    userr = User.objects.filter(username=username).first()

    # 所有房子
    house = User_weivilla.objects.count()


    # 所有用户
    user = User.objects.count()

    #评论
    pinglun = user_Blog.objects.count()

    # 所有推荐
    shejishi1 = User_stylist.objects.count()

    shejishi = User_stylist.objects.all()[0:42:1]

    return render(request, "index.html", context={
        'username': username,
        'dbss': dbs,
        "user": user,
        "house": house,
        "shejishi1": shejishi1,
        "shejishi": shejishi,
        "userr":userr,
        "pinglun":pinglun,
        'session': request.session , # 传入session数据
        'beishu1':beishu1
    })



# faq页面
def faq(request):
    return render(request, "faq.html")


# 注册页面
def register(request):
    if request.method=="GET":
        form = UserForm()
        return render(request, "register.html", context={"form": form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get("code")
            print("=====")
            scode = request.session.get('code')
            print(code,scode)
            if code.lower() != scode.lower():
                return render(request, "register.html", context={"form": form
                                                              ,"msg":"验证码输入有误"})
            else:
                del form.cleaned_data['recpassword']
                value = form.cleaned_data['password']
                print(value)
                form.cleaned_data["password"] = hashlib.sha1(value.encode("utf8")).hexdigest()
                print(form.cleaned_data)
                del form.cleaned_data['code']
                User.objects.create(**form.cleaned_data)

                return render(request,'login.html')

        return render(request, "register.html", context={"form": form})



# 登录页面
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)  # 用户输入的姓名和密码
        print("++++++++++")

        password = hashlib.sha1(password.encode("utf8")).hexdigest()
        print(password)

        request.session["username"] = username

        user = User.objects.filter(username=username, password=password)
        if user:
            return redirect(reverse('a'))
        else:
            return render(request, "login.html", {'msg': "用户名或密码错误"})
    return render(request, "login.html")





# 登出页面
def logout(request):
    del request.session['username']  # 退出删除session
    return redirect(reverse('a'))


# 联系我们页面
def contact(request):
    username = request.session.get("username")
    request.session["username"] = username
    return render(request, "contact.html", context={
        "username": username,
        'session': request.session
    })


# 获取验证码
def getcode(request):
    # 自己画图片。初始化画笔和画布
    mode = 'RGB'
    size = (180, 60)
    # 调取颜色
    red = get_color()
    green = get_color()
    blue = get_color()
    bg_color = (red, green, blue)
    # 准备画布
    image = Image.new(mode, size, color=bg_color)  # 准备画布
    draw = ImageDraw(image, mode=mode)  # 画笔
    # 字体
    font = ImageFont.truetype(font=settings.FONT_PATH, size=50)
    code = generate_code()  # 产生验证码

    request.session['code'] = code
    # 往画布画验证码
    # 取一个，画一个fill填充颜色
    for a in range(4):
        fill_color =(get_color(), get_color(), get_color())
        draw.text(xy=(47 * a, 0), text=code[a], font=font, fill=fill_color)

    for a in range(500):
        fill_color = (get_color(), get_color(), get_color())
        import random
        #位置
        position= (random.randrange(201), random.randrange(81))
        # 画点
        draw.point(xy=position,fill=fill_color)


    #   字节IO
    by = BytesIO()
    image.save(by,'png')
    return HttpResponse(by.getvalue(), content_type='image/png')







# 修改密码页面
def change(request):
    username = request.session.get("username")

    if request.method == "POST":

        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('recpassword')

        print(pwd1,pwd2)
        print("++++++++")
        if pwd1 != pwd2 :
            return render(request, "change-password.html", {'msg': "密码输入不一致"})
        else:
            pwd1 =hashlib.sha1(pwd1.encode("utf8")).hexdigest()
            u1 = User.objects.get(username=username)
            u1.password =pwd1
            u1.save()
            return redirect(reverse('login'))

    return render(request, "change-password.html",context={
                  'session': request.session,
                    'username': username

    })
