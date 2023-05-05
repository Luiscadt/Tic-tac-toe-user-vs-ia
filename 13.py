#----- Importar bibilotecas -------------------
import time
import random
import os

#----- Inicio del juego / SELECCION DE FICHAS -----------------------

def inicio_juego():
    print("Bienvenido al juego de Tic Tac Toe")
    time.sleep(1)

    while True:
        ficha = input("Seleccione ficha : X o O : ")
        ficha = ficha.upper()
        if ficha == "X":
            humano = "X"
            ordenador = "O"
            break
        elif ficha == "O":
            humano = "O"
            ordenador = "X"
            break
        else:
            print("Selecciona una ficha posible")
    return(humano, ordenador)


#----- CREACION DE TABLERO -----------------------

def tablero():
    print("TRES EN RAYA")
    print()
    print("      |         |      ")
    print("1 {}   |2   {}   |3  {} ".format(matriz[0], matriz[1], matriz[2]))
    print("      |         |      ")
    print("-----------------------")
    print("      |         |      ")
    print("4 {}   |5   {}   |6  {} ".format(matriz[3], matriz[4], matriz[5]))
    print("      |         |      ")
    print("-----------------------")
    print("      |         |      ")
    print("7 {}   |8   {}   |9  {} ".format(matriz[6], matriz[7], matriz[8]))
    print("      |         |      ")


#-----  DEFINE FINALES DE PARTIDA -----------------------

def empate(matriz):
    empate = True
    i = 0
    while (empate == True and i < 9):
        if matriz[i] == " ":
            empate = False
        i += 1
        
    return empate

def victoria(matriz):
    ganador = False
    if matriz[0] == matriz[1] == matriz[2] != " ":
        ganador = True
    elif matriz[3] == matriz[4] == matriz[5] != " ":
        ganador = True
    elif matriz[6] == matriz[7] == matriz[8] != " ":
        ganador = True
    elif matriz[0] == matriz[3] == matriz[6] != " ":
        ganador = True
    elif matriz[1] == matriz[4] == matriz[7] != " ":
        ganador = True
    elif matriz[2] == matriz[5] == matriz[8] != " ":
        ganador = True
    elif matriz[0] == matriz[4] == matriz[8] != " ":
        ganador = True
    elif matriz[2] == matriz[4] == matriz[6] != " ":
        ganador = True
    if ganador == True:
        return True
    else:
        return False

#-----  MOVIMIENTOS -----------------------

def movmiento_jugador():
    while True:
        posiciones = [0,1,2,3,4,5,6,7,8]
        casilla= int(input("Selecciona una casilla : "))
        if casilla not in posiciones:
            print("Selecciona una casilla posible")
        
        else:
            if matriz[casilla-1] == " ":
                matriz[casilla-1] = humano
                break
            else:
                print("Esa casilla ya esta ocupada")

def movmiento_ordenador():
    posiciones = [0,1,2,3,4,5,6,7,8]
    casilla = 9
    parar = False
    for i in posiciones:
        copia = list(matriz)
        if copia[i] == " ":
            copia[i]= ordenador
            if victoria(copia) == True:
                casilla = i
    
    if casilla == 9:
        for j in posiciones:
            copia = list(matriz)
            if copia[j]== " ":
                copia[j]= humano
            if victoria(copia) == True:
                casilla = i
                 
    if casilla == 9:
        while(not parar):
            casilla = random.randint(0,8)
            if matriz[casilla] == " ":
                parar = True
    matriz[casilla] = ordenador

#-----  DESARROLLO DE LA PARTIDA -----------------------

while True:
    matriz = [" "," "," "," "," "," "," "," "," "]
    os.system("clear")
    humano, ordenador = inicio_juego()
    partida = True
    ganador = 0

    while partida:
        ganador = ganador+1
        os.system("clear")
        tablero()
        
        if victoria(matriz):
            if ganador % 2 == 0:
                print("Gana el jugador!!")
                print("Felicidades")
                print("Reiniciando...")
                time.sleep(5)
                partida= False
            else:
                print("Gana el ordenador!!")
                print("Fin del juego")
                print("Perdiste")
                print("Reiniciando...")
                time.sleep(5)
                partida = False
        elif empate(matriz):
            print("Empate")
            print("Fin del juego")
            print("Reiniciando...")
            time.sleep(5)
            partida = False
        elif ganador%2 == 0:
            print("El ordenador esta pensando...")
            time.sleep(2)
            movmiento_ordenador()
        else:
            movmiento_jugador()