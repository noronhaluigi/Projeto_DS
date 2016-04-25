# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:28:25 2016

@author: Luigi
"""

import tkinter as tk

class Tabulero:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha!")        
        self.window.geometry("350x370")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
        self.window.rowconfigure(3, minsize=20, weight=1)
        texto_jogada = tk.Text(self.window)
        texto_jogada.configure(text= jogadas_turnos(self))
        texto_jogada.configure(font="Courier 20 bold")        
        texto_jogada.grid(row=3,sticky = "ew" )
       
       
        x = 1
        def jogada_turnos(self, x):   
            if x//2 == x/2:
                print("Próxima jogada: X")
                return 1
            else:
                print("Próxima jogada: O")
                return 1
        
        x += jogada_turnos(self, x)
         


        botão1 = tk.Button(self.window)
        botão1.configure(text=" ")
        botão1.configure(command=self.jogada)
        botão1.grid(row=0, column=0, sticky="nsew")

        botão2 = tk.Button(self.window)
        botão2.configure(text=" ")
        botão2.configure(command=self.jogada)
        botão2.grid(row=0, column=1, sticky="nsew")


        botão3 = tk.Button(self.window)
        botão3.configure(text=" ")
        botão3.configure(command=self.jogada)
        botão3.grid(row=0, column=2, sticky="nsew")
        
        botão4 = tk.Button(self.window)
        botão4.configure(text=" ")
        botão4.configure(command=self.jogada)
        botão4.grid(row=1, column=0, sticky="nsew")
        
        botão5 = tk.Button(self.window)
        botão5.configure(text=" ")
        botão5.configure(command=self.jogada)
        botão5.grid(row=1, column=1, sticky="nsew")
        
        botão6 = tk.Button(self.window)
        botão6.configure(text=" ")
        botão6.configure(command=self.jogada)
        botão6.grid(row=1, column=2, sticky="nsew")

        botão7 = tk.Button(self.window)
        botão7.configure(text=" ")
        botão7.configure(command=self.jogada)
        botão7.grid(row=2, column=0, sticky="nsew")
        
        botão8 = tk.Button(self.window)
        botão8.configure(text=" ")
        botão8.configure(command=self.jogada)
        botão8.grid(row=2, column=1, sticky="nsew")
        
        botão9 = tk.Button(self.window)
        botão9.configure(text=" ")
        botão9.configure(command=self.jogada)
        botão9.grid(row=2, column=2, sticky="nsew")

    def iniciar(self):
        self.window.mainloop()

    def jogada(self):
        return True


    def reinicia(self):
        return True


jogo = Tabulero()
jogo.iniciar()