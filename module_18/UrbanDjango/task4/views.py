from django.shortcuts import render  # type: ignore


# Create your views here.
def platform2(request):
    context = {
        'title': 'Platform2',
        'header': 'Главная страница',
    }
    return render(request, 'fourth_task/platform2.html', context)


def store2(request):
    context = {
        'title': 'Store2',
        'header': 'Игры',
        'store': ['The Elden Ring', 'Tekkin 8', 'Gran Turismo 7'],
    }
    return render(request, 'fourth_task/store2.html', context)


def cart2(request):
    context = {
        'title': 'Cart2',
        'header': 'Корзина',
        'catr_is_empty': 'Извините, ваша корзина пуста',
    }
    return render(request, 'fourth_task/cart2.html', context)
