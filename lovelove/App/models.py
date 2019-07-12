from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 用户表  django默认是不可空，flask默认可空
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=256)
    user_sex = ((0,"男"),(1,"女"))
    sex = models.IntegerField(default=0,choices=user_sex)
    email = models.EmailField(max_length=20,null=True)
    phone = models.CharField(max_length=11,null=True)
    regtime = models.DateTimeField(auto_now_add=True)
    usertype =((0,"普通用户"),(1,"管理员"))
    type = models.IntegerField(default=0,choices=usertype)
    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"

#
# 别墅特征表
class User_villalist(models.Model):
    tid = models.AutoField(primary_key=True)
    bedroom = models.IntegerField()  # 卧室
    bedroom_photo = models.CharField(max_length=500,null=True,default='/static/assets/img/icon/bed.png')  #卧室图片
    washhouse = models.IntegerField()  # 洗衣房
    garage = models.IntegerField()  # 车库
    garage_photo = models.CharField(max_length=500,null=True,default='/static/assets/img/icon/cars.png')  #车库图片
    bathroom = models.IntegerField()  # 浴室
    bathroom_photo = models.CharField(max_length=500,null=True,default='/static/assets/img/icon/shawer.png')  #浴室图片
    swimming = models.IntegerField()  # 游泳池
    lawn = models.IntegerField()  # 草坪
    bikeway = models.IntegerField()  # 自行车道

    def __str__(self):
        return str(self.tid)

    class Meta:
        db_table = 'user_villalist'
#
#
#全部未售别墅
class User_weivilla(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(unique=True,max_length=50)
    money = models.IntegerField()
    area = models.IntegerField()
    weivilla_photo = models.CharField(max_length=500,default='/static/assets/img/demo/property-1.jpg')  #别墅默认图片

    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = 'user_weivilla'



#博客表
class Blog(models.Model):
    bid = models.AutoField(primary_key=True)  # 博客id主键
    title = models.CharField(unique=True, max_length=30)  # 博客标题
    contect = models.CharField(max_length=300)  # 博客内容
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, to_field='username')  # 评论人用户表username
    ptime = models.DateTimeField(auto_now=True)  # 评论时间
    pcontect = models.CharField(max_length=250)  # 评论内容
    pphoto = models.CharField(max_length=500)  # 头像图片
    htime = models.DateTimeField(auto_now=True)  # 回复时间
    hcontect = models.CharField(max_length=250)  # 回复内容

    def __str__(self):
        return str(self.bid)

    class Meta:
        db_table = 'user_blog'

  #推荐别墅表
class User_tuijian(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    name = models.CharField(unique=True,max_length=50)
    money= models.IntegerField(null=True)
    tuijian_photo = models.CharField(max_length=500,null=True,default='/static/assets/img/demo/small-property-2.jpg')  #别墅默认图片

    class Meta:
        db_table = 'user_tuijian'



# #设计师表
class User_stylist(models.Model):
    sname =models.CharField(unique=True,max_length=50) #姓名
    stype = models.CharField(max_length=20)# 级别
    semail = models.EmailField(max_length=30)# 邮箱
    sphone = models.CharField(max_length=11) # 电话
    saddress =  models.CharField(max_length=200) # 地址
    signature =  models.CharField(max_length=200)   # 个性签名
    sphoto = models.CharField(max_length=200)   #个人头像

    class Meta:
        db_table = 'user_stylist'


 #评论页面
class user_Blog(models.Model):
    bid = models.AutoField(primary_key=True)  # 评论id主键
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, to_field='username')  # 评论人用户表username
    ptime = models.DateTimeField(auto_now=True)  # 评论时间
    pcontect = models.CharField(max_length=250)  # 评论内容
    pphoto = models.CharField(max_length=500,default="{% static 'assets/img/client-face2.png'%}")  # 头像图片

    def __str__(self):
        return str(self.bid)

    class Meta:
        db_table = 'user_Blog'



#别墅详情表

class User_xiangqing(models.Model):
    id = models.AutoField(unique=True,primary_key=True)#别墅id
    name = models.CharField(unique=True,max_length=50)#别墅名字
    money= models.IntegerField(null=True)  #别墅金额
    miaoshu = models.CharField(max_length=500)
    photo = models.CharField(max_length=500,null=True,default='/static/assets/img/property-1/property3.jpg"')  #别墅默认图片

    class Meta:
        db_table = 'user_xiangqing'