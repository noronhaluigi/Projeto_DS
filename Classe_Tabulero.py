# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:28:25 2016

@author: Luigi
"""

import tkinter as tk
from Ep3 import Jogo_da_Velha


import tkinter.messagebox as tkm
class Tabulero:
    def __init__(self):
        
        self.Velha = Jogo_da_Velha()        
        
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
       
        self.jogada = tk.Label(self.window, width= 50, text = "Proximo jogador: X", anchor = "w")
        self.jogada.grid(row=3, column=0, columnspan=3)
        


        self.botão1 = tk.Button(self.window)
        self.botão1.configure(text=" ")
        self.botão1.configure(command=self.Caso_B1)
        self.botão1.grid(row=0, column=0, sticky="nsew")

        self.botão2 = tk.Button(self.window)
        self.botão2.configure(text=" ")
        self.botão2.configure(command=self.Caso_B2)
        self.botão2.grid(row=0, column=1, sticky="nsew")

        self.botão3 = tk.Button(self.window)
        self.botão3.configure(text=" ")
        self.botão3.configure(command=self.Caso_B3)
        self.botão3.grid(row=0, column=2, sticky="nsew")
        
        self.botão4 = tk.Button(self.window)
        self.botão4.configure(text=" ")
        self.botão4.configure(command=self.Caso_B4)
        self.botão4.grid(row=1, column=0, sticky="nsew")
        
        self.botão5 = tk.Button(self.window)
        self.botão5.configure(text=" ")
        self.botão5.configure(command=self.Caso_B5)
        self.botão5.grid(row=1, column=1, sticky="nsew")
        
        self.botão6 = tk.Button(self.window)
        self.botão6.configure(text=" ")
        self.botão6.configure(command=self.Caso_B6)
        self.botão6.grid(row=1, column=2, sticky="nsew")

        self.botão7 = tk.Button(self.window)
        self.botão7.configure(text=" ")
        self.botão7.configure(command=self.Caso_B7)
        self.botão7.grid(row=2, column=0, sticky="nsew")
        
        self.botão8 = tk.Button(self.window)
        self.botão8.configure(text=" ")
        self.botão8.configure(command=self.Caso_B8)
        self.botão8.grid(row=2, column=1, sticky="nsew")
        
        self.botão9 = tk.Button(self.window)
        self.botão9.configure(text=" ")
        self.botão9.configure(command=self.Caso_B9)
        self.botão9.grid(row=2, column=2, sticky="nsew")

    def Resultados(self):
        if self.jogada["text"] == "Proximo Jogador: X":
            self.jogada["text"] = "Proximo Jogador: O"
        
        if self.jogada["text"] == "Proximo Jogador: O":
            self.jogada["text"] = "Proximo Jogador: X"
                
        if self.Velha.verifica_ganhador()==1:
            tkm.showinfo(message = "Parabéns jogador X! Você ganhou!")
            self.jogada["text"]="Proximo Jogador: X"
            self.reinicia()
            self.Velha.jogador = "O"
            self.Velha.limpa_jogadas()
            
        if self.Velha.verifica_ganhador()==2:
            tkm.showinfo(message = "Parabéns jogador O! Você ganhou!")
            self.jogada["text"]="Proximo Jogador: O"
            self.reinicia()
            self.Velha.jogador = "X"
            self.Velha.limpa_jogadas()
            
        if self.Velha.verifica_ganhador()==0:
            tkm.showinfo(message = "Deu velha!")
            self.jogada["text"]="Proximo Jogador: X"
            self.reinicia()
            self.Velha.jogador = "O"
            self.Velha.limpa_jogadas()
              
    def B_1_Clickado(self):
        self.Velha.recebe_jogada(0,0)
        self.botão1.configure(text = self.Velha.jogador, state = "disabled") 
        self.Velha.verifica_ganhador()
            
    def B_2_Clickado(self):
        self.Velha.recebe_jogada(0,1)
        self.botão2.configure(text = self.Velha.jogador, state = "disabled")
        self.Velha.verifica_ganhador()
        
    def B_3_Clickado(self):
        self.Velha.recebe_jogada(0,2)
        self.botão3.configure(text = self.Velha.jogador, state = "disabled") 
        self.Velha.verifica_ganhador()
        
    def B_4_Clickado(self):
        self.Velha.recebe_jogada(1,0)
        self.botão4.configure(text = self.Velha.jogador, state = "disabled")    
        self.Velha.verifica_ganhador()
        
    def B_5_Clickado(self):
        self.Velha.recebe_jogada(1,1)
        self.botão5.configure(text = self.Velha.jogador, state = "disabled")   
        self.Velha.verifica_ganhador()
        
    def B_6_Clickado(self):
        self.Velha.recebe_jogada(1,2)
        self.botão6.configure(text = self.Velha.jogador, state = "disabled")    
        self.Velha.verifica_ganhador()
        
    def B_7_Clickado(self):
        self.Velha.recebe_jogada(2,0)
        self.botão7.configure(text = self.Velha.jogador, state = "disabled") 
        self.Velha.verifica_ganhador()
        
    def B_8_Clickado(self):
        self.Velha.recebe_jogada(2,1)
        self.botão8.configure(text = self.Velha.jogador, state = "disabled")
        self.Velha.verifica_ganhador()
        
    def B_9_Clickado(self):
        self.Velha.recebe_jogada(2,2)
        self.botão9.configure(text = self.Velha.jogador, state = "disabled")
        self.Velha.verifica_ganhador() 
    
    def Caso_B1(self):
        self.B_1_Clickado()
        return self.Resultados()    
    def Caso_B2(self):
        self.B_2_Clickado()
        return self.Resultados()
    def Caso_B3(self):
        self.B_3_Clickado()
        return self.Resultados()
    def Caso_B4(self):
        self.B_4_Clickado()
        return self.Resultados()
    def Caso_B5(self):
        self.B_5_Clickado()
        return self.Resultados()    
    def Caso_B6(self):
        self.B_6_Clickado()
        return self.Resultados()
    def Caso_B7(self):
        self.B_7_Clickado()
        return self.Resultados()
    def Caso_B8(self):
        self.B_8_Clickado()
        return self.Resultados()
    def Caso_B9(self):
        self.B_9_Clickado()
        return self.Resultados()







    def iniciar(self):
        self.window.mainloop()


        
    def reinicia(self):
        self.botão1.configure(text = "", state="normal")

        self.botão2.configure(text = "", state="normal")

        self.botão3.configure(text = "", state="normal")

        self.botão4.configure(text = "", state="normal")

        self.botão5.configure(text = "", state="normal")

        self.botão6.configure(text = "", state="normal")

        self.botão7.configure(text = "", state="normal")

        self.botão8.configure(text = "", state="normal")

        self.botão9.configure(text = "", state="normal") 

                


Velha = Tabulero()
Velha.iniciar()