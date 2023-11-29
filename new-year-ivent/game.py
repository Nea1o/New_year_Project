#!/usr/bin/python3.12
import tkinter
from tkinter import ttk
import random
from read_dict import (result_output, result_output_and_times)
import os


def main():
    result_dict = {}
    if os.stat("result_dict.txt") != 0:
        with open("result_dict.txt", "r") as file_dict:
            for line in file_dict:
                print(line)
                k_and_v = line.split(" - ")
                result_dict[k_and_v[0]] = k_and_v[1].strip()

    def show_message(*event):
        def rand_int():
            number_point = random.choice([100, 100, 100, 100, 100, 150, 150, 150, 200, 300])
            return number_point

        point = rand_int()
        label["text"] = entry.get()
        number_card = label["text"]
        result_output_and_times(number_card, point)
        result_dict[number_card] = result_dict.setdefault(number_card, 0) + point
        result_output(result_dict)
        with open("result_dict.txt", "w", encoding="utf-8") as result_file_dict:
            for elem in sorted(result_dict.items()):
                string = f"{elem[0]} - {elem[1]}"
                print(string, file=result_file_dict)
            print(result_dict)


    root = tkinter.Tk()
    bg = tkinter.PhotoImage(file="background1.png")
    bg_label_main = tkinter.Label(root, image=bg)
    bg_label_main.place(x=0, y=0)
    label_welcome = tkinter.Label(root, text="Welcome")
    label_welcome.pack(pady=50)
    frame1 = tkinter.Frame(root)
    frame1.pack(pady=20)
    root.title("Новогодняя акция!!!")
    root.geometry("800x800")

    entry = ttk.Entry()
    entry.place(height=30, width=100, x=350, y=90)

    label = ttk.Label()
    label.place(height=30, width=100, x=350, y=650)

    bt1 = tkinter.Button(text="Click me!1")
    bt1.place(height=100, width=200, x=100, y=200)
    bt1.bind("<ButtonPress-1>", show_message)

    root.mainloop()
    return


if __name__ == "__main__":
    main()
