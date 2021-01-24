import tkinter
import os
from tkinter import filedialog
import pydev
from tkinter import Tk
import tkinter as tk
import random
import colorama
from colorama import Fore, Back, Style
from tkinter import messagebox
import turtle


def tkinterWin(title="", background="", widthxheight=""):
    root = tk.Tk()
    root.title(title)
    root.geometry(widthxheight)
    root.configure(background=background)
    print("application started")

    root.mainloop()


def P(message):
    print(message)


def Addition(num1="", num2="", num3=""):
    print(num1 + num2 + num3)


def Substraction(num1="", num2="", num3=""):
    print(num1 - num2 - num3)


def Multiplication(num1="", num2="", num3=""):
    print(num1 * num2 * num3)


def Division(num1="", num2="", num3=""):
    print(num1 / num2 / num3)


def Combine(a, b, c):
    print(a, b, c)


def askname(First="", Last=""):
    x = input(First)
    y = input(Last)
    z = "your Full name is:" + x + y
    print(z)


def asknum(First="", Last=""):
    x = input(First)
    a = int(x)
    y = input(Last)
    b = int(y)
    z = a + b
    print(z)


def tkinterDialog(title=""):
    root = Tk()
    root.title(title)
    root.geometry("1920x1080")
    root.resizable(False, False)

    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File")

    root.mainloop()


def math_add(a, b, c, d, ):
    print(a + b + c + d)

def math_sub(a, b, c, d, ):
    print(a - b - c - d)

def math_mul(a, b, c, d):
    print(a * b * c * d)

def math_div(num1, num2, num3, num4):
    print(num1 / num2 / num3 / num4)

def init():
    import colorama
    from colorama import Fore, Back, Style
    print("success")

def tkinterBut():
    print("Button")

def tkinterLabel(title="", geometry="", bg="", Label_text="", Label_font="", Label_color=""):
    root = Tk()
    root.title(title)
    root.geometry(geometry)
    root.configure(background=bg)

    my_label = tk.Label(root, fg=Label_color,font=Label_font,text=Label_text)
    my_label.pack()

    root.mainloop()

def tkinterMenu():
    print("a main menu")

def tkinterText(title="", geometry="", bg=""):
    root = Tk()
    root.title(title)
    root.geometry(geometry)
    root.configure(background=bg)

    my_text = tk.Text(root, width=1920, height=1080)
    my_text.pack()


    root.mainloop()

def tkintercav():
    print("simple Canvas")

def tkinter():
    print("all tkinter fun")

def Create_input(text1="",text2="",lastOption=""):
    x = input(text1)
    b = input(text2)
    print(lastOption, x + b)

def I(text="",):
    input(text)

def I_restart(text=""):
    for i in range(1000000):
        input(text)

def math_SAD(text1="", text2=""):
    print(text1+text2)

def O(Output="" , text1="", text2=""):
    print(Output + text1 + text2)

def Command():
    print("pydev.Output, pydev.math_SAD, pydev.P, pydev.I, pydev.Command(Current), pydev(Add3, Sub2, Mut3, div3, Add2, Sub3, Mut2, div2)")

def Add3(num1, num2, num3):
    print(num1 + num2 + num3)


def Sub2(num1, num2):
    by = num1 - num2
    print(by)

def Mut3(num1, num2, num3):
    print(num1 * num2 * num3)

def div3(num1, num2, num3):
    print(num1 / num2 / num3)


def Add2(num1, num2):
    print(num1 + num2)


def Sub3(num1, num2, num3):
    by = num1 - num2 - num3
    print(by)


def Mut2(num1, num2):
    print(num1 * num2)


def div2(num1, num2):
    print(num1 / num2)

def Accept(Print=()):
    print(Print)
    input("")

def Output(Output="", a="", b=""):
    print(Output + a + b)

def develop(title=" ", version=""):
    print("Pydev Python " + version + title + " All right reserved")

traceback = "Traceback (most recent call last): "

def traceback_error(traceback):
    print(traceback)

def commands(command=""):
    func = command
    print(func)

def Unrecognized_Input(Input=""):
    command = input(Input)
    if command in ["print("")", "p"]:
        command = "p"
    elif command in ["main", "m"]:
        command = "m"
    else:
        print("this command is not recognized as a command of input. ")
        commands()
    return command

def Random(a, b):
    p = random.randint(a,b)
    print(p)

def Draw(text1="", text2="", Draw=""):
    print("Drawing text... ")


    input(text1 + Draw + text2 + "$$")

def print_Red(Print=""):
    colorama.init()
    print(Fore.RED)
    print(Print)

def print_Yellow(Print=""):
    colorama.init()
    print(Fore.YELLOW)
    print(Print)

def print_Blue(Print=""):
    colorama.init()
    print(Fore.BLUE)
    print(Print)

def traceback():
    print("Traceback error")


def print_Black(Print=""):
    colorama.init()
    print(Fore.BLACK)
    print(Print)


def print_White(Print=""):
    colorama.init()
    print(Fore.WHITE)
    print(Print)


def print_Cyan(Print=""):
    colorama.init()
    print(Fore.CYAN)
    print(Print)

def colors():
    print(Fore.RED)
    print("red")
    print(Fore.BLACK)
    print("black")
    print(Fore.YELLOW)
    print("yellow")
    print(Fore.CYAN)
    print("cyan")
    print(Fore.BLUE)
    print("blue")
    print(Fore.WHITE)
    print("white")

def LIGHTMAGENTA_EX(first="", word="" + Style.RESET_ALL):
    print(first + Back.LIGHTMAGENTA_EX + word + Style.RESET_ALL)

def tkinter_alert(Title="", message=""):
    messagebox.askyesno(title=Title, message=message)

def print_value(Text="", Range=""):
    print(Text)

    for i in range(Range):
        print(Text)

def Input_value(Text="", Output="", Range=""):
    for i in range(Range):
        print(Style.RESET_ALL)
        input(Text)
        print(Fore.BLUE)
        print(Output)

def Turtle():
    turtle.mainloop()

def pydev_window(Title="", bg="",size=""):
    root = Tk()
    root.title(Title)
    root.geometry(size)
    root.configure(background=bg)
    root.resizable(True, True)
    root.iconbitmap("images/Graphicloads-Colorful-Long-Shadow-Book.ico")

    root.mainloop()

def create_Commands(Input="", command="", Output=""):

    name = input(Input)

    if name == command:
        print(Output)

def create_Commands_print(Input="", func=""):

    Name = "wow"

    name = input(Input)

    if name == func:
        print(Name)



def command_sys(command=""):
    os.system(command)

def join(Input=""):
    print("")
    input(Input)

def create_Commands_repeat(Input="", command="", Output="", repeat=""):

    for i in range(repeat):

        name = input(Input)

        if name == command:
            print(Output)

def create_Commands_if(Input="", command="", Output="", repeat=""):

    for i in range(repeat):

        name = input(Input)

        if name == command:
            print(Output)

answer = "==========="

def Draw_LINE(Line=answer, text1="", text2=""):
    input(text1 + answer + text2)

brackets = "()"

def Draw_Brackets():

    input("()")

