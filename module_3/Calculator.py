# 2023/10/15 00:00|Функции практика часть 2 (Калькулятор)

import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(values):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    if num2 == 0:
        res = 0
    else:
        res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('280x120')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=2, height=1, command=add)
button_add.place(x=160, y=85)
button_sub = tk.Button(window, text='-', width=2, height=1, command=sub)
button_sub.place(x=185, y=85)
button_mul = tk.Button(window, text='*', width=2, height=1, command=mul)
button_mul.place(x=210, y=85)
button_div = tk.Button(window, text='/', width=2, height=1, command=div)
button_div.place(x=235, y=85)

number1_entry = tk.Entry(window, width=16)
number1_entry.place(x=160, y=10)
number2_entry = tk.Entry(window, width=16)
number2_entry.place(x=160, y=35)
answer_entry = tk.Entry(window, width=16)
answer_entry.place(x=160, y=60)

number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=10, y=10)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=10, y=35)
answer = tk.Label(window, text='Результат:')
answer.place(x=10, y=60)

window.mainloop()
