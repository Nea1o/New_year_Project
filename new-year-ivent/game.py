#!/usr/bin/python3.12

from tkinter import *


def main():
    root = Tk()
    bg = PhotoImage(file="background1.png")
    bg_label_main = Label(root, image=bg)
    bg_label_main.place(x=0, y=0)
    label_welcome = Label(root, text="Welcome")
    label_welcome.pack(pady=50)
    frame1 = Frame(root)
    frame1.pack(pady=20)
    root.title("Новогодняя акция!!!")
    root.geometry("1000x1000")
    root.mainloop()
    return


if __name__ == "__main__":
    main()
