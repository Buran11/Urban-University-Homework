from django.shortcuts import render  # type: ignore


# Create your views here.
def platform(request):
    title = 'Platform'
    header = 'Главная страница'
    m_main = 'Главная'
    m_store = 'Магазин'
    m_cart = 'Корзина'

    return render(request, 'third_task/platform.html', {
        'title': title,
        'headr': header,
        'm_main': m_main,
        'm_store': m_store,
        'm_cart': m_cart
    })


def store(request):
    title = 'Store'
    header = 'Игры'
    b_back = 'На главную'
    return render(request, 'third_task/store.html', {
        'title': title,
        'header': header,
        'b_back': b_back
    })


def cart(request):
    title = 'Cart'
    header = 'Корзина'
    catr_is_empty = 'Извините, ваша корзина пуста'
    b_back = 'На главную'
    return render(request, 'third_task/cart.html', {
        'title': title,
        'header': header,
        'catr_is_empty': catr_is_empty,
        'b_back': b_back
    })
