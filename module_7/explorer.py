'''
Попробуйте добавить меню к вашему блокноту с пунктами "info" и "about".
В пункте "info" должно быть написано, как пользоваться вашим блокнотом,
а в пункте "about" — информация об авторе и версии программы.
Это будет задание для самостоятельной проработки.
'''

import tkinter
import os
from tkinter import filedialog
from tkinter import Menu

menu_info_text = "Для открытия файла нужно нажать кнопку\
\n\"Выбрать файл\".\n\
В открывшемся окне нужно выбрать\nфайл.txt.\n\
Программа выведит полный путь к нему."


def select_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Выберите файл", filetypes=((
            "Текстовый файл", "*.txt"), ("Все файлы", "*.*")))
    text['text'] += '' + filename
    os.startfile(filename)


def menu_info():
    window_info = tkinter.Tk()
    window_info.title("Информация о программе")
    window_info.geometry("250x150")
    window_info.configure(bg="silver")
    window_info.resizable(False, False)
    text_info = tkinter.Label(window_info,
                              text=menu_info_text, height=5, width=35, background="silver")
    text_info.grid(column=1, row=2)
    window_info.mainloop()


def menu_about():
    window_about = tkinter.Tk()
    window_about.title("Информация о программе")
    window_about.geometry("250x150")
    window_about.configure(bg="silver")
    window_about.resizable(False, False)
    text_about = tkinter.Label(window_about,
                               text="Версия: 1.0\nАвтор: Ионов В.О.", height=10,
                               width=35, background="silver")
    text_about.grid(column=1, row=1)
    window_about.mainloop()


window = tkinter.Tk()
window.title("Проводник")
window.geometry("450x150")
window.configure(bg="black")
window.resizable(False, False)
text = tkinter.Label(window, text="Файл: ", height=5,
                     width=65, background="silver")
text.grid(column=1, row=1)
button_select = tkinter.Button(
    window, text="Выбрать файл", width=20, height=3, command=select_file)
button_select.grid(column=1, row=2, pady=5)

# Menu
window.option_add("*tearOff", False)

main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label="Info", command=menu_info)
file_menu.add_command(label="About", command=menu_about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

main_menu.add_cascade(label="Menu", menu=file_menu)


window.config(menu=main_menu)
window.mainloop()
