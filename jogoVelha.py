import os
import random
from colorama import Fore, Back, Style

#variaveis globais
jogarnovamente = "s"  #indica se o jogador quer jogar novamente
jogadas = 0           #indica o numero de jogadas
quemJoga = 2          #jogador = 2 | maquina = 1
maxJogadas= 9         #numero maximo de jogadas do jogo da velha é 9
vit = "n"             #indica se o jogador ganhou
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " +  velha[0][2])
    print("   ----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   ----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogjoga():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit

    if quemJoga == 2 and jogadas<maxJogadas:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        
        try:
            while velha[linha][coluna] != " ":
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
            velha[linha][coluna] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida")

def cpuJoga():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit

    if quemJoga==1 and jogadas<maxJogadas:
        linha = int(random.randrange(0, 3))
        coluna = int(random.randrange(0, 3))

        while velha[linha][coluna] != " ":
            linha = int(random.randrange(0, 3))
            coluna = int(random.randrange(0, 3))
        velha[linha][coluna] = "O"
        quemJoga = 2
        jogadas += 1

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        
        #Verificar em linhas
        ilinha = icoluna = 0
        while ilinha < 3:
            soma = 0
            icoluna = 0
            while icoluna < 3:
                if velha[ilinha][icoluna] == s:
                    soma +=1
                icoluna += 1
            if soma == 3:
                vitoria = s
                break
            ilinha += 1
        if vitoria != "n":
            break
        
        #Verificar coluna
        ilinha = icoluna = 0
        while icoluna < 3:
            soma = 0
            ilinha = 0
            while ilinha < 3:
                if velha[ilinha][icoluna] == s:
                    soma +=1
                ilinha += 1
            if soma == 3:
                vitoria = s
                break
            icoluna += 1
        if vitoria != "n":
            break
        
        #Verificar diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s
            break

        #verificar diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria

def redefinir():
    global jogadas
    global quemJoga
    global velha
    global maxJogadas
    global vit
    jogadas = 0           
    quemJoga = 2          
    maxJogadas= 9         
    vit = "n"             
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarnovamente == "s" or jogarnovamente == "S":
    while True:
        tela()
        jogjoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if vit != "n" or jogadas >= maxJogadas:
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW )
    if vit=="X" or vit=="O":
        print("Resultado: Jogador " + vit + " venceu")
    else:
        print("Resultado: Empate")

    jogarnovamente = input(Fore.BLUE + "Jogar novamente? [s/n]" + Fore.RESET)
    redefinir()