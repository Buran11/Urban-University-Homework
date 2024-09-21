cart = []


def add_to_cart(item_name, item_price, item_quantity=1):
    global cart
    item = {
        'name': item_name,
        'price': item_price,
        'quantity': item_quantity
    }
    cart.append(item)
    print(f'Добавлен товар: {item_name}, цена:',
          f'{item_price}, количество: {item_quantity}')


def calculate_total_price(item):
    if not item:
        return 0
    else:
        first_item = item[0]
        return first_item['price'] * first_item['quantity'] + calculate_total_price(item[1:])


def checkout(*items):
    for item in items:
        add_to_cart(*item)


def customer_info(**info):
    print('Информация о покупателе')
    for key, value in info.items():
        print(f'{key}: {value}')


def remove_from_cart(item_name):
    global cart
    items_to_keep = []
    for item in cart:
        if item['name'] == item_name:
            continue
        else:
            items_to_keep.append(item)
    cart = items_to_keep
    print(f'Товар {item_name} удален из корзины')


def apply_discount(discount_func):
    global cart
    for item in cart:
        original_price = item['price']
        item['price'] = discount_func(item['price'])
        print(f'Скидка применена на {item['name']}.',
              f' Цена {original_price} -> {item['price']}')


def ten_percent_discount(price):
    return price * 0.9


add_to_cart('Телевизор', 30500)
add_to_cart('Нотбук', 70000, 2)

total = calculate_total_price(cart)
print(f'Итоговая сумма корзины {total}')

checkout(('Телефон', 58800), ('Планшет', 64200))

customer_info(first_name='Вася', last_name='Пупкин',
              city='Москва', email='pup@bk.ru', phone='123-45-67')

remove_from_cart('Нотбук')

apply_discount(ten_percent_discount)
