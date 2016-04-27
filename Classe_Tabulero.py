# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:28:25 2016

@author: Luigi
"""

import tkinter as tk
from Ep3 import Jogo_da_Velha
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
        
        x = Jogo_da_Velha()
        self.window.rowconfigure(3, minsize=20, weight=1)
        texto_jogada = tk.Label(self.window)
        texto_jogada.configure(text= x.recebe_jogada())
        texto_jogada.configure(font="Courier 20 bold")     
        texto_jogada.grid(row=3,column=0, columnspan=3,sticky = "nsew" )
        
         


        botão1 = tk.Button(self.window)
        botão1.configure(text=" ")
        botão1.configure(command=self.jogador)
        botão1.grid(row=0, column=0, sticky="nsew")

        botão2 = tk.Button(self.window)
        botão2.configure(text=" ")
        botão2.configure(command=self.jogador)
        botão2.grid(row=0, column=1, sticky="nsew")


        botão3 = tk.Button(self.window)
        botão3.configure(text=" ")
        botão3.configure(command=self.jogador)
        botão3.grid(row=0, column=2, sticky="nsew")
        
        botão4 = tk.Button(self.window)
        botão4.configure(text=" ")
        botão4.configure(command=self.jogador)
        botão4.grid(row=1, column=0, sticky="nsew")
        
        botão5 = tk.Button(self.window)
        botão5.configure(text=" ")
        botão5.configure(command=self.jogador)
        botão5.grid(row=1, column=1, sticky="nsew")
        
        botão6 = tk.Button(self.window)
        botão6.configure(text=" ")
        botão6.configure(command=self.jogador)
        botão6.grid(row=1, column=2, sticky="nsew")

        botão7 = tk.Button(self.window)
        botão7.configure(text=" ")
        botão7.configure(command=self.jogador)
        botão7.grid(row=2, column=0, sticky="nsew")
        
        botão8 = tk.Button(self.window)
        botão8.configure(text=" ")
        botão8.configure(command=self.jogador)
        botão8.grid(row=2, column=1, sticky="nsew")
        
        botão9 = tk.Button(self.window)
        botão9.configure(text=" ")
        botão9.configure(command=self.jogador)
        botão9.grid(row=2, column=2, sticky="nsew")

    def iniciar(self):
        self.window.mainloop()

    def click_botao(self, botao) :
        print("O botão {0} foi clickado").format(botao)
        botao.configure(text=self.jogador)
        
    def reinicia(self):
        botão1.configure(text = "", state="normal")
        botão2.configure(text = "", state="normal")
        botão3.configure(text = "", state="normal")
        botão4.configure(text = "", state="normal")
        botão5.configure(text = "", state="normal")
        botão6.configure(text = "", state="normal")
        botão7.configure(text = "", state="normal")
        botão8.configure(text = "", state="normal")
        botão9.configure(text = "", state="normal") 

                


jogo = Tabulero()
jogo.iniciar()