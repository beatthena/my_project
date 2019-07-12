import hashlib
import re
from django import forms

#用户表单
from django.core.exceptions import ValidationError

from App.models import User

#验证密码单个字段，value传入的密码
def yanzheng_password(value):
    if re.match(r"\d+$",value):   #正则验证密码是否纯数字
        raise ValidationError("密码不能由纯数字组成")
    else:
        return value

#验证手机号码格式
def yanzheng_phone(value):
    if not re.match(r"^((13[0-9])|(17[0-1,6-8])|(15[^4,\\D])|(18[0-9]))\d{8}$",value):
        raise ValidationError("手机号码不正确，请重新输入")
    else:
        return value





class UserForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,
                               max_length=10,min_length=3,
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}),
                                error_messages={
                                    "required":"必填",
                                    "min_length":"用户名最小3位",
                                    "max_length" : "用户名最大10位"
                                })

    password = forms.CharField(label="用户密码",required=True,
                               max_length=10,min_length=3,validators=[yanzheng_password],
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入用户密码'}),#如何不指定是明文的
                               error_messages={
                                   "required": "必填",
                                   "min_length": "用户密码最小3位",
                                   "max_length": "用户密码最大10位"
                               })

    recpassword = forms.CharField(label="确认密码", required=True,
                               max_length=10, min_length=3,
                               widget=forms.PasswordInput(attrs={'placeholder': '请确认用户密码'}),  # 如何不指定是明文显示的
                               )
    sex = forms.ChoiceField(label='性别',choices=[(0,'女'),(1,'男')],initial=0,widget=forms.RadioSelect, required=False)



    email = forms.EmailField(label="邮箱",widget=forms.EmailInput(attrs={'placeholder': '请输入邮箱'}),required=False,
                             error_messages={
                                 "invalid":"邮箱格式错误"
                             })

    phone = forms.CharField(label="手机号码",validators=[yanzheng_phone],min_length=11,widget=forms.TextInput(attrs={'placeholder': '请输入手机号'}),
                            required=False,error_messages={
            "min_length":"至少11位"
        })
    #验证码
    code = forms.CharField(label="验证码",max_length=4,min_length=4,
                           widget=forms.TextInput(attrs={'placeholder': '请输入验证码'}),
                           error_messages={
        "max_length":"验证码必须4位",
        "min_length":"验证码必须4位"
    })



    type = forms.ChoiceField(label="用户类别",choices=[(0,"普通用户"),(1,"管理员")],initial=0,widget=forms.RadioSelect,
                            required=False)




    # 验证两次密码不一致,全局验证
    def clean(self):
        pwd1 = self.cleaned_data.get("password")
        pwd2 = self.cleaned_data.get("recpassword")
        print(pwd1, pwd2)
        if pwd1 != pwd2:
            raise ValidationError({"recpassword":"密码输入不一致"})
        else:
            return self.cleaned_data






class adminUserForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,
                               max_length=10,min_length=3,
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}),
                                error_messages={
                                    "required":"必填",
                                    "min_length":"用户名最小3位",
                                    "max_length" : "用户名最大10位"
                                })

    password = forms.CharField(label="用户密码",required=True,
                               max_length=10,min_length=3,validators=[yanzheng_password],
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入用户密码'}),#如何不指定是明文的
                               error_messages={
                                   "required": "必填",
                                   "min_length": "用户密码最小3位",
                                   "max_length": "用户密码最大6位"
                               })