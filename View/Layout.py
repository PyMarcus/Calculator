import ttkbootstrap
from tkinter import *
from ttkbootstrap import *


class Calculator(Frame):
    """
    Interface
    """
    mainframe = Frame()
    visorframe = Frame(mainframe, width="80", height="100")
    button789frame = Frame(mainframe)
    button456frame = Frame(mainframe)
    button123frame = Frame(mainframe)

    @classmethod
    def visor(cls):
        visor = Entry(cls.visorframe, width="50", font=("Arial", 15), justify=RIGHT)
        visor.configure(background='white')
        visor.grid(row=0, column=0)
        return visor.pack(pady=20, padx=10)

    @classmethod
    def buttons789(cls):
        button7 = ttkbootstrap.Button(cls.button789frame, bootstyle="light", text="7", padding=10,width=10 )
        button7.grid(row=0, column=0, padx=10, pady=10)

        button8 = ttkbootstrap.Button(cls.button789frame, bootstyle="light", text="8", padding=10, width=10)
        button8.grid(row=0, column=1, padx=10, pady=10)

        button9 = ttkbootstrap.Button(cls.button789frame, bootstyle="light", text="9", padding=10, width=10)
        button9.grid(row=0, column=2, padx=10, pady=10)

    @classmethod
    def buttons456(cls):
        button7 = ttkbootstrap.Button(cls.button456frame, bootstyle="light", text="4", padding=10, width=10)
        button7.grid(row=0, column=0, padx=10, pady=10)

        button8 = ttkbootstrap.Button(cls.button456frame, bootstyle="light", text="5", padding=10, width=10)
        button8.grid(row=0, column=1, padx=10, pady=10)

        button9 = ttkbootstrap.Button(cls.button456frame, bootstyle="light", text="6", padding=10, width=10)
        button9.grid(row=0, column=2, padx=10, pady=10)

    @classmethod
    def buttons123(cls):
        button7 = ttkbootstrap.Button(cls.button123frame, bootstyle="light", text="1", padding=10, width=10)
        button7.grid(row=0, column=0, padx=10, pady=10)

        button8 = ttkbootstrap.Button(cls.button123frame, bootstyle="light", text="2", padding=10, width=10)
        button8.grid(row=0, column=1, padx=10, pady=10)

        button9 = ttkbootstrap.Button(cls.button123frame, bootstyle="light", text="3", padding=10, width=10)
        button9.grid(row=0, column=2, padx=10, pady=10)

    @classmethod
    def main(cls):
        Calculator.visor()
        cls.visorframe.pack()
        cls.buttons789()
        cls.button789frame.pack()
        cls.buttons456()
        cls.button456frame.pack()
        cls.buttons123()
        cls.button123frame.pack()
        cls.mainframe.pack()


if __name__ == '__main__':
    style = Style('darkly')
    master = style.master
    master.title('Python Calculator')
    master.geometry('380x400')
    calculator = Calculator(master)
    calculator.main()
    calculator.mainloop()
