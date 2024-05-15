import math

#EJERCICIO 1:

#1.1)
def imprimir_hola_mundo():
    print ("Hola mundo!")

#1.2)
def imprimir_un_verso ():
    print ("straight\n from\n the\n tortured\n poets\n department") 

#1.3)
def raizDe2 ():
    return round((math.sqrt(2)),4)

#1.4)
def factorial_de_dos()-> int:
    return math.factorial(2)
    

#1.5)
def perimetro () -> float:
    return 2*(math.pi)




#EJERCICIO 2:

#2.1)
def imprimir_saludo (nombre: str) -> str:
    print ("hola" + str(" ") + str(nombre)) 

#2.2)
def raiz_cuadrada_de (numero: float) -> float:
    return math.sqrt(numero)
    
#2.3)
def fahrenheit_a_celsius (t: float) -> float:
    return ((t-32)*5)/9


