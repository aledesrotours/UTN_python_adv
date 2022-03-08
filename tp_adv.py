from tkinter import *
from tk_adv import Ventanita


class Principal():

    def __init__(self, windows):
        self.root_principal = windows
        Ventanita(self.root_principal)


if __name__ == "__main__":
    root = Tk()
    obj = Principal(root)
    root.mainloop()
