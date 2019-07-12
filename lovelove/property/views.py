from django.shortcuts import render

# Create your views here.
#属性
from App.models import User_tuijian, User_villalist, User_weivilla, User_stylist, User_xiangqing


def property(request,id=1):
    username = request.session.get("username")
    dbb = User_tuijian.objects.all()
    bieshu = User_weivilla.objects.all()
    qbtz = User_villalist.objects.all()
    qbtz1 = User_villalist.objects.get(pk=id)
    beishu1 = User_weivilla.objects.get(pk=id)
    sheji = User_stylist.objects.get(pk=id)
    xiangqing = User_xiangqing.objects.get(pk=id)
    print(xiangqing)
    print(1)
    return render(request, "property.html", context={
        'dbb': dbb,
        'qbtz': qbtz,
        "bieshu": bieshu,
        "username": username,
        'session': request.session,
        'sheji': sheji,
        'xiangqing': xiangqing,
        'beishu1': beishu1,
        'qbtz1': qbtz1
    })


def property2(request,id=1):
    username = request.session.get("username")
    dbb = User_tuijian.objects.all()
    bieshu = User_weivilla.objects.all()
    qbtz = User_villalist.objects.all()
    qbtz1 = User_villalist.objects.get(pk=id)
    beishu1 = User_weivilla.objects.get(pk=id)
    sheji = User_stylist.objects.get(pk=id)
    xiangqing = User_xiangqing.objects.get(pk=id)
    print(xiangqing)
    print(1)
    return render(request, "property2.html", context={
        'dbb': dbb,
        'qbtz': qbtz,
        "bieshu": bieshu,
        "username": username,
        'session': request.session,
        'sheji': sheji,
        'xiangqing': xiangqing,
        'beishu1': beishu1,
        'qbtz1': qbtz1
    })


def property3(request,id=1):
    username = request.session.get("username")
    dbb = User_tuijian.objects.all()
    bieshu = User_weivilla.objects.all()
    qbtz = User_villalist.objects.all()
    qbtz1 = User_villalist.objects.get(pk=id)
    beishu1 = User_weivilla.objects.get(pk=id)
    sheji = User_stylist.objects.get(pk = id)
    xiangqing = User_xiangqing.objects.get(pk=id)
    print(xiangqing)
    print(1)
    return  render(request,"property3.html",context={
                    'dbb': dbb,
                    'qbtz': qbtz,
                    "bieshu": bieshu,
                   "username":username,
                   'session': request.session,
                  'sheji'   : sheji,
                  'xiangqing' : xiangqing,
                 'beishu1' :beishu1,
        'qbtz1':qbtz1
    })