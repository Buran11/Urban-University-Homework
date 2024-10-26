import datetime
import json
from random import randint

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']

# for file in files:
#     for _ in range(100_000):
#         res.append(randint(0, 10000))
#     with open(file, 'w', encoding='utf-8') as f:
#         json.dump(res, f)
#     res = []


def main():
    res_to_count = []
    start = datetime.datetime.now()

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            res_to_count.extend(data)
    sum(res_to_count)
    end = datetime.datetime.now()
    return end - start


time_calc = []
for i in range(100):
    time_calc.append(main())
print(sum([calc.microseconds for calc in time_calc]) / len(time_calc))

# 48349.73
