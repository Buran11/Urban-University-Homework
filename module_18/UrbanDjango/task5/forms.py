from django import forms  # type: ignore


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите Логин')
    password = forms.CharField(max_length=8, label='Введите Пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите Пароль')
    age = forms.IntegerField(label='Введите Возраст')
    
