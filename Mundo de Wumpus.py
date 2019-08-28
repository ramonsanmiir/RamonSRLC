import os
from os.path import exists
import time
import random
import sys
from time import sleep
import os.path
import pygame.mixer, pygame.time
mixer = pygame.mixer
time1 = pygame.time
main_dir = os.path.split(os.path.abspath(__file__))[0]

def main(file_path=None):

    if file_path is None:
        file_path = os.path.join(main_dir,
                                 'data',
                                 'tema1.wav')
    mixer.init(11025) #raises exception on fail
    sound = mixer.Sound(file_path)
    channel = sound.play()

   
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()

def tiro_som():
    file_path = os.path.join(main_dir,
                                 'data',
                                 'tiro.wav')
    mixer.init(11025) #raises exception on fail
    sound = mixer.Sound(file_path)
    channel = sound.play()

def grito_som():
    file_path = os.path.join(main_dir,
                                 'data',
                                 'grito.wav')
    mixer.init(11025) #raises exception on fail
    sound = mixer.Sound(file_path)
    channel = sound.play()
   
    



#Menu 
def menu():
   mensagem = "Bem vindo ao mundo de Wumpus, para jogar, digite {!play}, para ver o top 5: {!ranking}, para ver as movimentações: {!controle} e para sair: {!sair}. Você também pode usar {!menu} a qualquer momento do jogo para sair do jogo e acessar aqui novamente!"
   print(mensagem)
   mensagem = input().lower()
   while True:
       if mensagem == "!play":
           jogo()
       elif mensagem == "!ranking":
           ranking = open("data/ranking_leitura.txt","r")
           ranking_leitura = ranking.readlines()
           for linhas in ranking_leitura:
               print(linhas)           
           mensagem = input("Volte a navegar no menu:").lower()
           continue
       elif mensagem == "!controle":
           controle = " W você vai para frente, A para a esquerda, S para baixo, D para a Direita. Caso queira atirar aperte T, garimpar G"
           print(controle)
           mensagem = input().lower()
           continue
       elif mensagem == "!menu":
           return menu()
       else:      
            mensagem = "Comando inválido, tente novamente."
            print(mensagem)
            mensagem = input().lower()

#Matriz impressa para o player

def player_inicial(matriz_player):

    matriz_player[len(matriz_player)-1][0] = " K"

def end_game(matriz_player, matriz):    
    text_print("********************MAPA ORIGINAL******************************\n")
    imprimir_matriz(matriz)
    text_print("********************SEUS CAMINHOS******************************\n")
    imprimir_matriz(matriz_player)
    print("      **************************************************       ")
    print("Sua pontuação foi igual a: ", pontos(matriz,matriz_player))
    ranking_(matriz,matriz_player)
  

def player_position(matriz_player):
    for j in range(len(matriz_player[0])):
        for i in range(len(matriz_player)):
            if matriz_player[i][j] == " K":
                player_linha = i
                player_coluna = j
                return player_linha, player_coluna

def contador(matriz_player):
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " V" or matriz[i][j] == " ^" or matriz[i][j] == " <" or matriz[i][j] == " >":
              contador = contador + 1
    return contador

def buraco_position(matriz):
    lista_buraco = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " *":
                lista_buraco.append([i,j])             
    return lista_buraco

def brisa_position(matriz):
    lista_brisa = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 9":
                lista_brisa.append([i,j])  
    return lista_brisa

def wumpus_position(matriz):
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 7":
                wumpus_linha = i
                wumpus_coluna = j
                return wumpus_linha, wumpus_coluna

def fedor_position(matriz):
    lista_fedor = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 6":
                lista_fedor.append([i,j])  
    return lista_fedor

def gold_position(matriz):
    lista_gold = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 5":
                lista_gold.append([i,j])  
    return lista_gold

def gold_fedor(matriz):
    lista_gold_fedor = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 4":
                lista_gold_fedor.append([i,j])  
    return lista_gold_fedor

def gold_brisa(matriz):
    lista_gold_brisa = []
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == " 8":
                lista_gold_brisa.append([i,j])  
    return lista_gold_brisa



def verificar(matriz_player,matriz):    
    if list(player_position(matriz_player)) in brisa_position(matriz):
        brisa_aviso = ("**Você está sentindo uma brisa, deve ter um buraco  por perto**\n")
        text_print(brisa_aviso)
        
    elif list(player_position(matriz_player)) in buraco_position(matriz):      
         end_game(matriz_player, matriz)
         end = "Você caiu em um buraco, deseja jogar novamente? Digite S para sim ou qualquer outra tecla para não:\n "
         text_print(end)
         game_over = input().upper()
        #Retirar 10000 mil pontos
         if game_over == "S":
             jogo()
         else:
              print("Até mais!")
              exit(0)

    elif player_position(matriz_player) == wumpus_position(matriz):        
        grito_som()
        end_game(matriz_player, matriz)    
        game_over = input("Você caiu em cima do monstro, deseja jogar novamente? Digite S para sim ou N para nao.").upper()
        
        #RETIRAR 10000 pts
        
        if game_over == "S":     
             jogo()
        else:
             print("Até mais!")
             exit(0)   

    elif list(player_position(matriz_player)) in fedor_position(matriz):
        fedor_aviso = ("**Há um cheiro estranho por aqui, é melhor tomar cuidado!**\n")
        text_print(fedor_aviso)  

    elif list(player_position(matriz_player)) in gold_position(matriz):
        ouro_aviso = ("**Há um brilho forte aqui, deve ter ouro!**\n")
        text_print(ouro_aviso) 
    
    elif list(player_position(matriz_player)) in gold_fedor(matriz):
        gf_aviso = ("**Há um brilho forte aqui, deve ter ouro! OPA, que cheiro é esse? O Wumpus se encontra por perto, melhor ter cuidado!!**\n")
        text_print(gf_aviso) 
    elif list(player_position(matriz_player)) in gold_brisa(matriz):
        gb_aviso = ("**Há um brilho forte aqui, deve ter ouro! OPA, aqui existe uma brisa forte também, existe algum buraco por perto!**\n")
        text_print(gb_aviso) 
     


#MOVIMENTOS       

def player_moveW(matriz_player,matriz):    
    player_linha = player_position(matriz_player)[0] 
    player_coluna = player_position(matriz_player)[1]
    matriz_player[player_linha][player_coluna] = " ^"
    matriz_player[player_linha-1][player_coluna] = " K"
    verificar(matriz_player,matriz)
    imprimir_matriz(matriz_player)
    WASD = input("").upper()
    return player_skill(WASD,matriz_player,matriz)

def player_moveA(matriz_player,matriz):    
    player_linha = player_position(matriz_player)[0] 
    player_coluna = player_position(matriz_player)[1]
    matriz_player[player_linha][player_coluna] = " <"
    matriz_player[player_linha][player_coluna-1] = " K"
    verificar(matriz_player,matriz)
    imprimir_matriz(matriz_player)
    WASD = input("").upper()
    return player_skill(WASD,matriz_player,matriz)

def player_moveS(matriz_player,matriz):    
    player_linha = player_position(matriz_player)[0] 
    player_coluna = player_position(matriz_player)[1]
    matriz_player[player_linha][player_coluna] = " V"
    matriz_player[player_linha+1][player_coluna] = " K"
    verificar(matriz, matriz_player)
    imprimir_matriz(matriz_player)
    WASD = input("").upper()
    return player_skill(WASD,matriz_player,matriz)

def player_moveD(matriz_player,matriz):    
    player_linha = player_position(matriz_player)[0] 
    player_coluna = player_position(matriz_player)[1]
    matriz_player[player_linha][player_coluna] = " >"
    matriz_player[player_linha][player_coluna+1] = " K"
    verificar(matriz_player,matriz)
    imprimir_matriz(matriz_player)
    WASD = input("").upper()
    return player_skill(WASD,matriz_player,matriz)

def player_moveT(matriz_player, matriz): 
    wumpus_linha = wumpus_position(matriz)[0]
    wumpus_coluna = wumpus_position(matriz)[1]
    player_linha = player_position(matriz_player)[0]
    player_coluna = player_position(matriz_player)[1]   
    destino = input("Digite o sentido do tiro, (N)ORTE, (S)ul, (L)este, (O)este.").upper()
    if destino == "N":

        if wumpus_linha < player_linha and wumpus_coluna == player_coluna:
            return True

        else:
            return  False

    elif destino == "S":     

         if wumpus_linha > player_linha and wumpus_coluna == player_coluna:
             return True

         else:
             return False

    elif destino == "L":  

         if wumpus_coluna > player_coluna and player_linha == wumpus_linha:
               return True

         else:
               return False

    elif destino == "O":    
         if wumpus_coluna < player_coluna and player_linha == wumpus_linha:      
               return True
         else:
               return False
    else:
         print("Sentido inválido.")
         return player_moveT(matriz_player, matriz)

def player_moveG(matriz_player, matriz): 
    gold = gold_position(matriz)
    player = list(player_position(matriz_player))
    if player in gold:
        return True
    else:
        return  False
    




#Habilidades

def player_skill(WASD, matriz_player,matriz):   
  player_linha = player_position(matriz_player)[0]
  player_coluna = player_position(matriz_player)[1]
  while True:
      if WASD == "W":
          if player_linha == 0:
             WASD = input("Não há como ir para frente, tente outro movimento: ").upper()
          else:         
               clear_time()
               return player_moveW(matriz_player, matriz)              
      elif WASD == "A":
           if player_coluna == 0:
               WASD = input("Não há como ir para a esquerda, tente outro movimento: ").upper()  
           else:
               clear_time()
               player_moveA(matriz_player, matriz)
      elif WASD == "S":
          if player_linha == (len(matriz)-1):
             WASD = input("Não há como ir para baixo, tente outro movimento: ").upper()
          else:
               clear_time()
               player_moveS(matriz_player, matriz)
      elif WASD == "D":
          if player_coluna == (len(matriz[0])-1):
              WASD = input("Não há como ir para a direita, tente outro movimento: ").upper()
          else:
               clear_time()
               player_moveD(matriz_player, matriz)
      elif WASD == "T":        
          acerto = player_moveT(matriz_player, matriz)
          if acerto == True:              
               tiro_som()
               pontos_tiro()
               pontos(matriz,matriz_player)
               print("Você acertou o wumpus! O jogo chegou ao fim, Você ganhou: 10000 pts.")  
               end_game(matriz_player, matriz)
               break
               #recorde
              
          else:
               tiro_som()
               print("Você errou o alvo! O jogo chegou ao fim.")
               pontos(matriz,matriz_player)
               end_game(matriz_player, matriz)
               pontos_wumpus = 0
               game_over = input("Caso queira jogar novamente digite S, caso não, digite N.").upper()
               if game_over == " S":
                   return jogo()
               else: 
                   exit(0)
               

      elif WASD == "G":
          acerto_gold = player_moveG(matriz_player, matriz)
          if acerto_gold == True:
              print("Você acaba de garimpar uma pepita de ouro. +1000 pontos!\n" )
              pontos_tiro()
              pontos(matriz,matriz_player)
              WASD = input("").upper()
              return player_skill(WASD,matriz_player,matriz)

          else:
              print("Nao há ouro aqui!\n")
              pontos(matriz,matriz_player)
              WASD = input("").upper()
              return player_skill(WASD,matriz_player,matriz)
      elif WASD == "!MENU":
          return menu()      
      elif WASD == "!CONTROLE":
           controle = " W você vai para frente, A para a esquerda, S para baixo, D para a Direita. Caso queira atirar aperte T, garimpar G"
           print(controle)
      else:
          WASD = input("A tecla digita não corresponde a nenhum comando, tente novamente: ").upper()
 
#Boas Vindas

def start_game(matriz_player):
      texto = "O mundo do Wumpus é caracterizado por um labirinto repleto de abismos, habitado por um terrível monstro, Wumpus.Além disso, o mundo também esconde perigosas armadilhas. O objetivo do jogo é matar o Wumpus, fugindo das armadilhas encontradas pelo caminho. Manter-se vivo é a principal tarefa para se concluir o objetivo. Porém, isso não será muito fácil, no interior da caverna, deve-se ficar muito atento as indicações de perigo uma vez que você é dotado de percepções, como por exemplo, você será capaz de sentir a brisa que sai dos abismos espalhados pela caverna ou sentir o mal-cheiro exalado pelo terrível Wumpus. Após essa perigosa busca, você poderá ir para o próximo nível para continuar acumulando barra de ouro e aumentar a aventura. Seu personagem será representado pela letra K, bom jogo! \n "
      text_animation(texto)
      time.sleep(3)     
      clear()
      text_print("Wumpus says: GRRRRRRRRRRRRRRRRRRRRRR \n")
      text_print("- É possível perceber que o Wumpus não está muito feliz, tenha uma boa jornada. " )
      imprimir_matriz(matriz_player)     
      time.sleep(2)
      print("\nAs movimentações se dão pelas teclas W(FRENTE), A (ESQUERDA), S(TRÁS), E D(DIREITA). Utilize a tecla T, para atirar. Para garimpar o ouro, aperte G.\n")
      time.sleep(7)
      clear()
      imprimir_matriz(matriz_player) 

def text_animation(texto):
    skip = input("Caso deseje pular a história, digite {!skip} agora, se não, aperte enter para prosseguir.")
    for i in texto:
        if skip == "!skip":
            break
        sleep(0.08)
        sys.stdout.write(i)
        sys.stdout.flush()

def text_print(texto):
    for i in texto:
        sleep(0.07)
        sys.stdout.write(i)
        sys.stdout.flush()
     


#Populando buraco

def buracos(porcentagem, matriz):
    range_matriz = len(matriz) - 1
    for i in range(porcentagem):        
        linha_buraco = random.randint(0,range_matriz)
        coluna_buraco = random.randint(0,range_matriz)        
        matriz[len(matriz)-1][0] = " K"
        while(matriz[linha_buraco][coluna_buraco] == " *"):
		        linha_buraco = random.randint(0,range_matriz)
		        coluna_buraco = random.randint(0,range_matriz)       
        while(matriz[linha_buraco][coluna_buraco] == " K"):
		        linha_buraco = random.randint(0,range_matriz)
		        coluna_buraco = random.randint(0,range_matriz)
        matriz[linha_buraco][coluna_buraco] = " *"
      


def arredondar(matriz):
    tam_matriz = len(matriz) * len(matriz[0])
    porcentagem = tam_matriz * 18/100
    if porcentagem > int(porcentagem):
        porcentagem = int(porcentagem + 1)
        return int(porcentagem)

    else:

        return int(porcentagem)



#Criando matriz



def cria_matriz(lin, col):   
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append(" 0")
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for m in matriz:
        print(m[:])


#Populando Wumpus

def wumpus(matriz):
    range_matriz = len(matriz) - 1   
    linha_wumpus = random.randint(0,range_matriz)
    coluna_wumpus = random.randint(0,range_matriz)        
    matriz[len(matriz)-1][0] = " K"
    for i in range(1):    
        while(matriz[linha_wumpus][coluna_wumpus] == " *"):
		        linha_wumpus = random.randint(0,range_matriz)
		        coluna_wumpus = random.randint(0,range_matriz)       
        while(matriz[linha_wumpus][coluna_wumpus] == " K"):
		        linha_wumpus = random.randint(0,range_matriz)
		        coluna_wumpus = random.randint(0,range_matriz)
        matriz[linha_wumpus][coluna_wumpus] = " 7"
       

    

#Brisa and Fedor

def permitir_pop(i,j,matriz):
    if (i-1)  >=  0 and (j-1) >= 0 and (i+1) < ( len(matriz) ) and (j+1) < (len(matriz)):
        return True
    else:
        return False




def brisa(matriz):   
    for j in range(len(matriz)):
        for i in range(len(matriz)):
            if matriz[i][j] == " *":              
                if permitir_pop(i,j,matriz) == True:
                    if matriz[i][j-1] == " *" :                 
                        matriz[i-1][j] = " 9"
                        matriz[i+1][j] = " 9"
                        matriz[i][j+1] = " 9"
                    elif  matriz[i-1][j] == " *":
                        matriz[i][j-1] = " 9"
                        matriz[i+1][j] = " 9"
                        matriz[i][j+1] = " 9"
                    elif matriz[i+1][j] == " *":
                        matriz[i][j-1] = " 9"
                        matriz[i-1][j] = " 9"
                        matriz[i][j+1] = " 9"
                    elif  matriz[i][j+1] == " *":
                        matriz[i][j-1] = " 9"
                        matriz[i-1][j] = " 9"
                        matriz[i+1][j] = " 9"                               
                    else:
                        matriz[i][j-1] = " 9"
                        matriz[i-1][j] = " 9"
                        matriz[i+1][j] = " 9"
                        matriz[i][j+1] = " 9"
                elif i == 0 and j == 0:
                    if matriz[0][1] == " *":
                        matriz[1][0] = " 9"
                        matriz[0][1] = " *"                   
                        matriz[1][1] = " 9"
                        matriz[0][2] = " 9"
                    elif matriz[0][1] == " *":
                        matriz[1][0] = " *"
                        matriz[0][1] = " 9"       
                    else:
                        matriz[1][0] = " 9"
                        matriz[0][1] = " 9"  
                elif j == (len(matriz[0]) -1) and i == 0:                
                     if matriz[0][len(matriz[0])-2] == " *":
                         matriz[0][len(matriz[0])-2] = " *"
                         matriz[1][len(matriz[0])-1] = " 9" 
                     else:
                         matriz[0][len(matriz[0])-2] = " 9"   
                         matriz[1][len(matriz[0])-1] = " 9"       
                elif i == ( len(matriz) - 1) and  j == (len(matriz[0])-1):
                     if matriz[len(matriz)-1][len(matriz[0])-2] == " *" :
                         matriz[len(matriz)-1][len(matriz[0])-2] = " *" 
                         matriz[len(matriz)-2][len(matriz[0])-1] = " 9"      
                     else:
                         matriz[len(matriz)-1][len(matriz[0])-2] = " 9" 
                         matriz[len(matriz)-2][len(matriz[0])-1] = " 9"    
                elif j == (len(matriz[0] )-1):
                   if  matriz[i][j-1] == " *" :
                        matriz[i][j-1] = " *"
                        matriz[i-1][j] = " 9"      
                   else:
                        matriz[i][j-1] = " 9"
                        matriz[i-1][j] = " 9"                       
                elif j == 0:
                    if matriz[i][j+1] == " *" :
                        matriz[i][j+1] = " *" 
                        matriz[i+1][j] = " 9"   
                        matriz[i-1][j] = " 9"
                    else:
                        matriz[i-1][j] = " 9"
                        matriz[i][j+1] = " 9" 
                        matriz[i+1][j] = " 9"        
                elif i == (len(matriz)-1) and j == 1:
                    if matriz[i-1][j] == " *" :
                        matriz[i-1][j] = " *" 
                        matriz[i][j+1] = " 9"   
                    else:
                        matriz[i-1][j] = " 9" 
                        matriz[i][j+1] = " 9"                  
                elif i == (len(matriz)-1):
                    if  matriz[i-1][j] == " *":
                        matriz[i-1][j] = " *"
                        matriz[i][j-1] = " 9"
                    else:
                        matriz[i-1][j] = " 9"
                        matriz[i][j-1] = " 9" 
    return matriz

def cria_matriz(lin, col):

  

    matriz = []

    for i in range(lin):

        linha = []

        for j in range(col):

            linha.append(" 0")

        matriz.append(linha)

        

    return matriz
def fedor(matriz):   
  
    for j in range(len(matriz)):
        for i in range(len(matriz)):
            if matriz[i][j] == " 7":              
                if permitir_pop(i,j,matriz) == True:
                    if matriz[i][j-1] == " *" :                 
                        matriz[i-1][j] = " 6"
                        matriz[i+1][j] = " 6"
                        matriz[i][j+1] = " 6"
                    elif  matriz[i-1][j] == " *":
                        matriz[i][j-1] = " 6"
                        matriz[i+1][j] = " 6"
                        matriz[i][j+1] = " 6"
                    elif matriz[i+1][j] == " *":
                        matriz[i][j-1] = " 6"
                        matriz[i-1][j] = " 6"
                        matriz[i][j+1] = " 6"
                    elif  matriz[i][j+1] == " *":
                        matriz[i][j-1] = " 6"
                        matriz[i-1][j] = " 6"
                        matriz[i+1][j] = " 6"                               
                    else:          
                        matriz[i][j-1] = " 6"
                        matriz[i-1][j] = " 6"
                        matriz[i+1][j] = " 6"
                        matriz[i][j+1] = " 6"
                elif i == 0 and j == 0:
                    if matriz[0][1] == " 7":
                        matriz[1][0] = " 6"
                        matriz[0][1] = " 6"                   
                        matriz[1][1] = " 6"
                        matriz[0][2] = " 6"
                    elif matriz[0][1] == " 7":
                        matriz[1][0] = " 7"
                        matriz[0][1] = " 6"       
                    else:
                        matriz[1][0] = " 6"
                        matriz[0][1] = " 6"  
                elif j == (len(matriz[0]) -1) and i == 0:                
                     if matriz[0][len(matriz[0])-2] == " 7":
                         matriz[0][len(matriz[0])-2] = " 7"
                         matriz[1][len(matriz[0])-1] = " 6" 
                     else:
                         matriz[0][len(matriz[0])-2] = " 6"   
                         matriz[1][len(matriz[0])-1] = " 6"       
                elif i == ( len(matriz) - 1) and  j == (len(matriz[0])-1):
                     if matriz[len(matriz)-1][len(matriz[0])-2] == " 7" :
                         matriz[len(matriz)-1][len(matriz[0])-2] = " 7" 
                         matriz[len(matriz)-2][len(matriz[0])-1] = " 6"      
                     else:
                         matriz[len(matriz)-1][len(matriz[0])-2] = " 6" 
                         matriz[len(matriz)-2][len(matriz[0])-1] = " 6"    
                elif j == (len(matriz[0] )-1):
                   if  matriz[i][j-1] == " 7" :
                        matriz[i][j-1] = " 7"
                        matriz[i-1][j] = " 6"      
                   else:
                        matriz[i][j-1] = " 6"
                        matriz[i-1][j] = " 6"                       
                elif j == 0:
                    if matriz[i][j+1] == " 7" :
                        matriz[i][j+1] = " 7" 
                        matriz[i+1][j] = " 6"   
                        matriz[i-1][j] = " 6"
                    else:
                        matriz[i-1][j] = " 6"
                        matriz[i][j+1] = " 6" 
                        matriz[i+1][j] = " 6"        
                elif i == (len(matriz)-1) and j == 1:
                    if matriz[i-1][j] == " 7" :
                        matriz[i-1][j] = " 7" 
                        matriz[i][j+1] = " 6"   
                    else:
                        matriz[i-1][j] = " 6" 
                        matriz[i][j+1] = " 6"                  
                elif i == (len(matriz)-1):
                    if  matriz[i-1][j] == " 7":
                        matriz[i-1][j] = " 7"
                        matriz[i][j-1] = " 6"
                    else:
                        matriz[i-1][j] = " 6"
                        matriz[i][j-1] = " 6" 
    return matriz
# BRISA = 9, BURACO = *, MONSTRO = 7, FEDOR = 6, GOLD = 5, fedor/gold = 4, brisa/gold = 8



#Clear
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

def clear_time():
    if os.name == "nt":
        time.sleep(0.2)
        os.system('cls')
    else:
        time.sleep(0.2)
        os.system("clear")

#Fonte



def colorir(x):   
    print("\033[31m",x,"\033[0;0m")    

def colorir_amarelo(x):
    print("\033[33m",x,"\033[0;0m")

def colorir_verde(x):
    print("\033[32m",x,"\033[0;0m")

def colorir_ciano(x):
    print("\033[36m",x,"\033[0;0m")

def colorir_menu(x):
    print("\033[35m",x,"\033[0;0m")


#Gold

def gold(matriz):
    range_matriz = len(matriz) - 1
    porcentagem = int(len(matriz)*len(matriz[0])/8)
    for i in range(porcentagem):        
        linha_gold = random.randint(0,range_matriz)
        coluna_gold = random.randint(0,range_matriz)              
        while(matriz[linha_gold][coluna_gold] == " *"):
                        linha_gold = random.randint(0,range_matriz)
                        coluna_gold = random.randint(0,range_matriz)             

        while(matriz[linha_gold][coluna_gold] == " 7"):
                        linha_gold = random.randint(0,range_matriz)
                        coluna_gold = random.randint(0,range_matriz)

        while(matriz[linha_gold][coluna_gold] == " K"):
                        linha_gold = random.randint(0,range_matriz)
                        coluna_gold = random.randint(0,range_matriz)        
        matriz[linha_gold][coluna_gold] =" 5"
        matriz[len(matriz)-1][0] = " K"
#Pontuação
def pontos_tiro():
    acerto = True
    return acerto

def pontos(matriz,matriz_player): 
    pont_end = 0
    p__gold = gold_position(matriz)
    player = player_position(matriz_player)
    acerto = pontos_tiro()
    acerto_g = pontos_tiro()
    p_lista =  list(player_position(matriz_player))
    w_position = wumpus_position(matriz)
    b_position = buraco_position(matriz)
    if player == w_position or p_lista in b_position:
         pont_end = (pont_end - 10000) 
    elif acerto == True: 
         pont_end = (pont_end + 10000) 
    elif acerto_g == True:
         pont_end = (pont_end + 1000) 
    else:
         pont_end = pont_end
    return str(pont_end)
#Ranking

def ranking():
    with open('ranking.txt') as arquivo_1, \
         open('ranking_2.txt') as arquivo_2, \
         open('ranking.txt', 'w') as saida:
         numeros_arquivo_1 = (int(numero.strip()) for numero in arquivo_1)
         numeros_arquivo_2 = (int(numero.strip()) for numero in arquivo_2)
         for a, b in zip(numeros_arquivo_1, numeros_arquivo_2):
            saida.write(f'{a}\n' if a >= b else f'{b}\n')
def ranking_(matriz,matriz_player):
    nome = input("Você está no livro dos recordes! Digite seu nome: ")
    if  exists('data/ranking_leitura.txt') == False:
        score = open('data/ranking_leitura.txt', 'w')
        score.write(nome + " "+pontos(matriz,matriz_player) + '\n')
        score.close()
        print('TOP 5' + nome  + pontos(matriz,matriz_player))
    else:
        score = open('data/ranking_leitura.txt', 'a')
        score.write(nome +" "+ pontos(matriz,matriz_player) + '\n')
        score.close()       
        


def jogo():
 
    dificuldade = int(input("Pressione 1 para fácil, 2 para médio e 3 para dificil: " ))
    while True:  
        if dificuldade == 1:            
            passo = 4      
        elif dificuldade == 2:
            passo = 6
        elif dificuldade == 3:
            passo = 10
        else:
           dificuldade = int(input("A dificuldade digitada não existe, tente novamente: "))
           continue         
        matriz_player = cria_matriz( passo, passo )
        matriz = cria_matriz( passo, passo )
        player_inicial(matriz_player)
        start_game(matriz_player)
        porcentagem = arredondar(matriz)
        buracos(porcentagem, matriz)
        brisa(matriz)
        wumpus(matriz)        
        fedor(matriz)
        gold(matriz)
        WASD = input("").upper()
        player_skill(WASD,matriz_player,matriz)
        break

menu()
