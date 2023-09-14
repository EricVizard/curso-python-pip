import random

contador = 0
key = False
eleccion = False
winPlayer = 0
winCPU = 0
jugadas = ["piedra", "papel", "tijera"]

while key == False:
    contador += 1
    print("*********************************")
    print(f"******* ROUND {contador} *******")
    print("*********************************")
    while eleccion == False:
        selectPlayer = input("¿Piedra, papel o tijera? ==> ").lower();
        if selectPlayer in jugadas:
            eleccion = True
        else:
            print("Esa jugada no existe, intenta de nuevo")
            eleccion = False
    selectCPU = random.choice(jugadas)
    print(f"CPU: {selectCPU}")

    if(selectPlayer == "piedra" and selectCPU == "tijera"):
        print("Gano jugador")
        winPlayer += 1
    elif(selectPlayer == "piedra" and selectCPU == "piedra"):
        print("Empate!")
    elif(selectPlayer == "piedra" and selectCPU == "papel"):
        print("Gano CPU")
        winCPU += 1
    elif(selectPlayer == "papel" and selectCPU == "piedra"):
        print("Gano jugador")
        winPlayer += 1
    elif(selectPlayer == "papel" and selectCPU == "papel"):
        print("Empate!")
    elif(selectPlayer == "papel" and selectCPU == "tijera"):
        print("Gano CPU")
        winCPU += 1
    elif(selectPlayer == "tijera" and selectCPU == "papel"):
        print("Gano jugador")
        winPlayer += 1
    elif(selectPlayer == "tijera" and selectCPU == "tijera"):
        print("Empate!")
    elif(selectPlayer == "tijera" and selectCPU == "piedra"):
        print("Gano CPU")
        winCPU += 1

    print(f"winPlayer: {winPlayer}")
    print(f"winCPU: {winCPU}")
    if(winPlayer == 3 or winCPU == 3):
        key = True
    eleccion = False 
    
