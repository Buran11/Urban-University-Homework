# 2023/11/15 00:00|Домашнее задание по теме "Режимы открытия файлов"

# import logging

class Product:
    ''' Базовый класс продукта '''

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    ''' Базовый класс магазина '''
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as f:
            # logging.info('Данные продука были получены = %s', f.read())
            return f.read()

    def add(self, *products):
        if not products:
            # logging.warning('Продукты не были добавлены в магазин')
            return
        for i in range(len(products)):
            with open(self.__file_name, 'r') as f:
                if str(products[i]) in f.read():
                    print(f'Продукт {products[i]} уже есть в магазине')
                    # logging.info('Продукт уже есть в магазине')
                    f.close
                    continue
                else:
                    with open(self.__file_name, 'a', encoding='utf-8') as f:
                        for product in products:
                            # logging.info('Продукт добавлен в магазин')
                            f.write(
                                f'{product.name}, {product.weight}, {product.category}\n')
                    f.close
                    break


# Точка входа
if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO,
    #                     format="%(asctime)s %(levelname)s %(message)s")
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
