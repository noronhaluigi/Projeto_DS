#Começando a parte do jogo do Ep3
#criando uma classe

class Jogo_da_Velha():
    def __init__(self):
        self.jogador = "O"
        self.B = [["z","z","z"],["z","z","z"],["z","z","z"]] 
        
    def recebe_jogada(self, linha, coluna):
        if self.B[linha][coluna]=="z":
            self.B[linha][coluna]=self.jogador
            if self.jogador=="X":
                self.jogador="O"
            elif self.jogador=="O":
                self.jogador="X"       
    
    def verifica_ganhador(self):
        if self.B[0][0]==self.B[0][1] and self.B[0][1]==self.B[0][2]:
            if self.B[0][0]=="O":
                return 1
            elif self.B[0][0]=="X":
                return 2
        elif self.B[1][0]==self.B[1][1] and self.B[1][1]==self.B[1][2]:
            if self.B[1][0]=="O":
                return 1
            elif self.B[1][0]=="X":
                return 2
        elif self.B[2][0]==self.B[2][1] and self.B[2][1]==self.B[2][2]:
            if self.B[2][0]=="O":
                return 1
            elif self.B[2][0]=="X":
                return 2
        elif  self.B[0][0]==self.B[1][0] and self.B[1][0]==self.B[2][0]:
            if self.B[0][0]=="O":
                return 1
            elif self.B[0][0]=="X":
                return 2              
        elif  self.B[0][1]==self.B[1][1] and self.B[1][1]==self.B[2][1]:
            if self.B[0][1]=="O":
                return 1
            elif self.B[0][1]=="X":
                return 2                     
        elif  self.B[0][2]==self.B[1][2] and self.B[1][2]==self.B[2][2]:
            if self.B[0][2]=="O":
                return 1
            elif self.B[0][2]=="X":
                return 2   
        elif self.B[0][0]==self.B[1][1] and self.B[1][1]==self.B[2][2]:
            if self.B[1][1]=="O":
                return 1
            elif self.B[1][1]=="X":
                return 2
        elif self.B[0][2]==self.B[1][1] and self.B[1][1]==self.B[2][0]:
            if self.B[1][1]=="O":
                return 1
            elif self.B[1][1]=="X":
                return 2
        else:
            if (self.B[0][0]!="z") and (self.B[0][1]!="z") and (self.B[0][2]!="z") and (self.B[1][0]!="z") and (self.B[1][1]!="z") and (self.B[1][2]!="z") and (self.B[2][0]!="z") and  (self.B[2][1]!="z") and (self.B[2][2]!="z"): 
                return 0
        
    def limpa_jogadas(self):
        if self.verifica_ganhador()==0 or self.verifica_ganhador()==1 or self.verifica_ganhador()==2:
            self.B=[["z","z","z"],["z","z","z"],["z","z","z"]]
            
    
                
                
                
                
                
                
                
                
        