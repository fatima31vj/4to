EJERCICIO 1:

#Inicio de juego
vida=1000 #vida inicial del personaje
energia = float(input("ingresa energia inicial"))

#Ingresa item que quiere levantar el personaje
item = input("que item levanta el personaje?(energizante o curacion):")
#Si la energia es menor a 50 se le suma 10 puntos

if item =="energizante":
     if energia < 50: 
        energia += 10
#Si la energia es 50 o mas se le suma 100 puntos
     else:
        energia *= 2

#Si item que agarra es "curacion" se le suma 100 puntos
elif item == "curacion":
     vida += 100

#Si el item no se reconoce el item no se realiza ningun cambio
else:
    print("item no reconocido. No se realiza ningun cambio")

#Estado final del personaje
print(f"vida final del personaje: {vida}")
print(f"energia final del personaje: {energia}")

ingresa energia inicia:l60
que item levanta el personaje?(energizante o curacion):curacion
vida final del personaje: 1100
energia final del personaje: 60.0


EJERCICIO 2:
El codigo simula el movimiento de un personaje en un mapa de dos dimensiones como si estuviera en un plano X/Y, segun la direccion y distancia que ingreso el usuario 
