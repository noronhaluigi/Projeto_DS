# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:28:25 2016

@author: Luigi
"""

import tkinter as tk

class Tabulero:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")        
        self.window.geometry("350x370")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        



    def iniciar(self):
        self.window.mainloop()



jogo = Tabulero()
jogo.iniciar()

