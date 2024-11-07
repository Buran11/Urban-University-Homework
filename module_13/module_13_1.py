import asyncio


async def start_strongman(name: str, power: int):
    num_ball = 1
    max_ball = 5
    delay = 1 / power
    print(f'Силач {name} начал соревнования.')
    while max_ball > 0:
        print(f'Силач {name} поднял {num_ball}.')
        await asyncio.sleep(delay)
        num_ball += 1
        max_ball -= 1
    print(f'Силач {name} закончил соревнования.')


async def start_turnament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_turnament())
