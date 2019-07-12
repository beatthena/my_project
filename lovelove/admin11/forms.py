from django import forms


class AdminForm(forms.Form):
    name = forms.CharField(label="用户名",required=True,
                               max_length=10,min_length=3,
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}),
                             error_messages={
                                    "required":"必填",
                                    "min_length":"用户名最小3位",
                                    "max_length" : "用户名最大10位"
                                })

    pwd = forms.CharField(label="用户密码",required=True,
                               max_length=10,min_length=3,
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入用户密码'}),#如何不指定是明文的
                               error_messages={
                                   "required": "必填",
                                   "min_length": "用户密码最小3位",
                                   "max_length": "用户密码最大6位"
                               })