from django.shortcuts import render  # type: ignore
from .forms import UserRegister


# Create your views here.
users = ['slava', 'masha', 'user2003']


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        greating = ''
        user_exists = False
        info = {}
        if str(password) != str(repeat_password):
            info['error'] = 'Пароли не совпадают'
        else:
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                for user in users:
                    if username == user:
                        user_exists = False
                        break
                    else:
                        user_exists = True
                if user_exists:
                    info = {'error': ''}
                    greating = f'Приветствуем, {username}!'
                else:
                    info = {'error': 'Пользователь уже существует'}

        context = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age,
            'greating': greating,
            'info': info['error'],
        }
        return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html')


def django_sign_up(request):
    info = {}
    greating = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            user_exists = False
            if str(password) != str(repeat_password):
                info['error'] = 'Пароли не совпадают'
            else:
                if int(age) < 18:
                    info['error'] = 'Вы должны быть старше 18'
                else:
                    for user in users:
                        if username == user:
                            user_exists = False
                            break
                        else:
                            user_exists = True
                    if user_exists:
                        info = {'error': ''}
                        greating = f'Приветствуем, {username}!'
                    else:
                        info = {'error': 'Пользователь уже существует'}
    else:
        form = UserRegister()
    context = {
        'form': form,
        'greating': greating,
        'info': info['error'],
    }
    return render(request, 'fifth_task/registration_page.html', context)
