from django.shortcuts import render  # type: ignore

# Create your views here.


def platform2(request):
    context = {
        'title': 'Platform2',
        'header': 'Главная страница',
        'm_main': 'Главная',
        'm_store': 'Магазин',
        'm_cart': 'Корзина'
    }

    return render(request, 'fourth_task/platform2.html', context)


def store2(request):
    context = {
        'title': 'Store2',
        'header': 'Игры',
        'b_back': 'На главную',
        'first_game': 'The Elden Ring',
        'second_game': 'Tekkin 8',
        'third_game': 'Gran Turismo 7'
    }
    return render(request, 'fourth_task/store2.html', context)


def cart2(request):
    context = {
        'title': 'Cart2',
        'header': 'Корзина',
        'catr_is_empty': 'Извините, ваша корзина пуста',
        'b_back': 'На главную'
    }
    return render(request, 'fourth_task/cart2.html', context)
