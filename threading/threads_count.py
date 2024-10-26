from threading import Thread
import json
import datetime

res = []
threads = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def worker(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        res.extend(data)


def main():
    start = datetime.datetime.now()

    for i in range(len(files)):
        t = Thread(target=worker, args=(files[i],))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = datetime.datetime.now()
    sum(res)
    return end - start


time_calc = []
for i in range(100):
    res = []
    time_calc.append(main())
print(sum([calc.microseconds for calc in time_calc]) / len(time_calc))

# 44990.15
