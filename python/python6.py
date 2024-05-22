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

#2.4)
def imprimir_dos_veces (estribillo: str):
    return 2*(estribillo + " ")

#2.5)
def es_multiplo_de (n: int, m: int) -> bool:
    if (n/m) == math.ceil(n/m): es_multiplo_de =True
    else: es_multiplo_de =False
    return es_multiplo_de       

#2.6)
def es_par (numero: int) -> bool:
    if es_multiplo_de (numero, 2): es_par =True
    else: es_par =False
    return es_par

#2.7)
def cantidad_de_pizzas (comensales: int, min_cant_de_porciones: int) -> int:
    if round((comensales*min_cant_de_porciones)/8) == (comensales*min_cant_de_porciones)/8: cantidad_de_pizzas =(comensales*min_cant_de_porciones)/8
    else: cantidad_de_pizzas =round((comensales*min_cant_de_porciones)/8)+1
    return cantidad_de_pizzas


#EJERCICIO 3:

#3.1)
def alguno_es_0 (numero1: int, numero2: int) -> bool:
    return (numero1 ==0) or (numero2 ==0) 

#3.2)
def ambos_son_0 (numero1: int, numero2: int) -> bool:
    return (numero1 ==0) and (numero2 ==0) 

#3.3)
def es_nombre_largo (nombre: str) -> bool:
    return ((len(nombre) >= 3)) and ((len(nombre)) <=8) 

#3.4)
def es_bisiesto (año: int) -> bool:
    return (es_multiplo_de (año,400)) or (es_multiplo_de (año,4) and (not (es_multiplo_de (año,400))))



#EJERCICIO 4:

def peso_pino (metros: float) -> float:
    if metros<=3: peso_pino=metros*100*3
    elif metros>3: peso_pino =900 + (metros-3)*100*2
    return peso_pino

def es_peso_util (peso: float) -> bool:
    return (peso>=400) and (peso<=1000)

def sirve_pino (metros: float) -> bool:
    return (metros>=(1.33)) and (metros<=(3.5))

def sirve_pino2 (metros: float) -> bool:
    return (peso_pino (metros)>=400) and (peso_pino (metros)<=1000)


