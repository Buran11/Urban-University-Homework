from django.shortcuts import render  # type: ignore
from .forms import UserRegister
from .models import Game, Buyer, News
from django.core.paginator import Paginator  # type: ignore


# Create your views here.
def news(request):
    news = News.objects.all().order_by('-data', '-time')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'News',
        'header': 'Новости',
        'page_obj': page_obj, }
    return render(request, 'fourth_task/news.html', context)


def sign_up_by_html(request):
    users = Buyer.objects.all()
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
                    if username == user.name:
                        user_exists = False
                        break
                    else:
                        user_exists = True
                if user_exists:
                    info = {'error': ''}
                    greating = f'Приветствуем, {username}!'
                    Buyer.objects.create(name=username, age=age, balance=0)
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
    users = Buyer.objects.all()
    info = {'error': ''}
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
                        if username == user.name:
                            user_exists = False
                            break
                        else:
                            user_exists = True
                    if user_exists:
                        info = {'error': ''}
                        greating = f'Приветствуем, {username}!'
                        Buyer.objects.create(name=username, age=age, balance=0)
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


def platform(request):
    context = {
        'title': 'Platform',
        'header': 'Главная страница',
    }
    return render(request, 'fourth_task/platform.html', context)


def store(request):
    games = Game.objects.all()
    context = {
        'title': 'Store',
        'header': 'Игры',
        'store': games,
    }
    return render(request, 'fourth_task/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'header': 'Корзина',
        'catr_is_empty': 'Извините, ваша корзина пуста',
    }
    return render(request, 'fourth_task/cart.html', context)
