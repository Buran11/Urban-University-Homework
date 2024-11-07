import time
import asyncio


# async def notification():
#     time.sleep(10)
#     print('До доставки осталось 10 минут')


# async def main():
#     task = asyncio.create_task(notification())
#     print('Собираемся в поездку')
#     print('Едем')

async def get_temp():
    print('Первое показание')
    await asyncio.sleep(2)
    print('25 C')


async def get_pres():
    print('Второе показание')
    await asyncio.sleep(4)
    print('101 kPa')


async def main():
    print('Старт')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_pres())
    await task1
    await task2
    print('Финиш')


start = time.time()
asyncio.run(main())
finish = time.time()
print(f'Время выполнения: {round(finish - start, 2)} секунд')


# asyncio.run(main())
