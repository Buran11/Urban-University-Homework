from django.shortcuts import render  # type: ignore


# Create your views here.
def platform(request):
    context = {
        'title': 'Platform',
        'header': 'Главная страница',
        'm_main': 'Главная',
        'm_store': 'Магазин',
        'm_cart': 'Корзина'
    }
    return render(request, 'third_task/platform.html', context)


def store(request):
    context = {
        'title': 'Store',
        'header': 'Игры',
        'b_back': 'На главную',
        'buy': 'Купить',
        'first_game': 'The Elden Ring',
        'second_game': 'Tekkin 8',
        'third_game': 'Gran Turismo 7'
    }
    return render(request, 'third_task/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'header': 'Корзина',
        'catr_is_empty': 'Извините, ваша корзина пуста',
        'b_back': 'На главную'
    }
    return render(request, 'third_task/cart.html', context)
