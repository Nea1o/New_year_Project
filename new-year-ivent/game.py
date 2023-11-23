#!/usr/bin/python3.12
import tkinter
import random


def main():
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
    bt1 = tkinter.Button(text="Click me!1")
    bt1.place(height=100, width=200, x=100, y=100)
    bt1.bind("<ButtonPress-1>", rand_int)
    bt2 = tkinter.Button(text="Click me!2")
    bt2.place(height=100, width=200, x=300, y=100)
    bt3 = tkinter.Button(text="Click me!3")
    bt3.place(height=100, width=200, x=500, y=100)
    root.mainloop()
    return


def rand_int(event):
    print(random.choice([100, 100, 100, 100, 100, 150, 150, 150, 200, 300]))
    return


if __name__ == "__main__":
    main()
