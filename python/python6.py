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


#EJERCICIO 5:

#5.1)
def devolver_el_doble_si_es_par (numero: int) -> int:
    if es_par (numero): devolver_el_doble_si_es_par =2*numero
    else: devolver_el_doble_si_es_par =numero
    return devolver_el_doble_si_es_par

#5.2)
def devolver_valor_si_es_par_sino_el_que_sigue1 (numero: int) -> int:
     if es_par (numero): devolver_valor_si_es_par_sino_el_que_sigue1 =numero 
     else: devolver_valor_si_es_par_sino_el_que_sigue1 =numero + 1 
     return devolver_valor_si_es_par_sino_el_que_sigue1

def devolver_valor_si_es_par_sino_el_que_sigue2 (numero: int) -> int:
     if es_par (numero): devolver_valor_si_es_par_sino_el_que_sigue2 =numero 
     if not(es_par (numero)): devolver_valor_si_es_par_sino_el_que_sigue2 = numero + 1 
     return devolver_valor_si_es_par_sino_el_que_sigue2     

#5.3)
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo91 (numero: int) -> int:
    if es_multiplo_de (numero,9): devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo91 =3*numero
    elif es_multiplo_de (numero,3): devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo91 =2*numero
    else: devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo91 =numero
    return devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo91

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo92 (numero: int) -> int:
    if es_multiplo_de (numero,9): devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo92 =3*numero    
    elif es_multiplo_de (numero,3): devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo92 =2*numero
    if not (es_multiplo_de (numero,3)) and not (es_multiplo_de (numero,9)): devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo92 = numero
    return devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo92

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo93 (numero: int) -> int:
    return (es_multiplo_de (numero,9) and (3*numero)) or (es_multiplo_de (numero,3) and (2*numero)) or (numero)

#5.4)
def lindo_nombre (nombre:str) -> str:
    if (len(nombre))>=5: lindo_nombre = "Tu nombre tiene muchas letras!"
    else: lindo_nombre = "Tu nombre tiene menos de 5 caracteres"
    return lindo_nombre

#5.5)
def elRango (numero: int) -> str:
    if numero<5: elRango ="Menor a 5"
    elif (numero>10) and (numero<=20): elRango ="Entre 10 y 20"
    elif(numero>20): elRango ="Mayor a 20"
    else: elRango = "No pertenece a elRango"
    return elRango

#5.6)
def destinoSexo (sexo: str, edad: int) -> str:
    if sexo=="F" and edad>=60: destinoSexo = "Andá de vacaciones"
    elif sexo=="F" and edad<60 and edad>=18: destinoSexo = "Te toca trabajar"
    elif sexo=="M" and edad>=65: destinoSexo = "Andá de vacaciones"
    elif sexo=="M" and edad<65 and edad>=18: destinoSexo = "Te toca trabajar"
    else: destinoSexo = "Andá de vacaciones"
    return destinoSexo



#EJERCICIO 6:

#6.1)
def numeros1a10 ():
    numero: int = 1
    while numero<=10:
        print (numero)
        numero += 1

#6.2)
def numeros10a40 ():
    numero: int = 1
    while numero <= 40:
        if es_par (numero) : 
            print (numero)
        numero += 1

#6.3)
def imprime_eco ():
    palabra = "eco"
    n = 1
    while n<=10:
        print(palabra)
        n += 1 


#6.4)
def despegue (numero: int) -> int:
    while numero >=1:
        print(numero)
        numero -= 1    
    print ("Despegue") 

#6.5)
def viaje_tiempo (partida: int, llegada: int) -> None:
    while partida>=llegada:
        if (partida - 1) > llegada:
            print("Viajó un año al pasado, estamos en el año: " + str (partida - 1))
        elif (partida - 1) == llegada:
            print("Viajó un año al pasado, estamos en el año: " + str (llegada))   
        partida -= 1
        
#6.6)
def viaje_aristoteles (partida: int) -> None:
    while partida>=(-384):
          if (partida - 20) > (-384):
            print("Viajó un año al pasado, estamos en el año: " + str (partida - 20))
          elif (partida - 20) == 384:
            print("Viajó un año al pasado, estamos en el año: " + str (384))   
          partida -= 20



#EJERCICIO 7:

#7.1)
def numeros1a10_2 ():
    for numero in range(1,11,1):
        print (numero)

#7.2)
def numeros10a40_2 ():
    for numero in range(10,42,2):
        print (numero)

#7.3)
def imprime_eco_2 ():
    palabra = "eco"
    for n in range(1,10,1):
        print(palabra)        

#7.4)
def despegue_2 (numero: int) -> int:
    for numero in range (numero,0,-1):
        print(numero)
    print("Despegue")

#7.5)
def viaje_tiempo_2 (partida: int, llegada: int) -> None:
    for partida in range(partida,llegada,-1):
        print("Viajó un año al pasado, estamos en el año: " + str (partida)) 

#7.6)
def viaje_aristoteles_2 (partida: int) -> None:
    for partida in range(partida,(-384),-20): 
        print("Viajó un año al pasado, estamos en el año: " + str (partida))    



#EJERCICIO 8:

#8.1)
def ocho_uno () -> int:
    x = 5
        #//Estado 1 x == 5
    y = 7
        #//Estado 2 y == 5
    x = x + y
        #//Estado 3 x == 12
    return x


#8.2)
def ocho_dos () -> int:
    x = 5
        #//Estado 1 x == 5
    y = 7
        #//Estado 2 y == 7
    z = x + y
        #//Estado 3 z == 12
    y = z*2
        #//Estado 4 y == 24
    return y      

#8.3)
def ocho_tres () -> str:
    x = 5
        #//Estado 1 x == 5
    y = 7
        #//Estado 2 y == 7
    x = "hora"
        #//Estado 3 x == "hora"
    y = x * 2
        #//Estado 4 y == "horahora"
    return y

#8.4)
def ocho_cuatro () -> bool:
    x = False
        #//Estado 1 x == False
    x = not (x)
        #//Estado 2 x == True
    res = x
        #//Estado 3 res == True
    return res    

#8.5)
def ocho_cinco () -> bool:
    x = False
        #//Estado 1 x == False
    x = not (x)
        #//Estado 2 x == True
    return x

#8.6)
def ocho_seis () -> bool:
    x = True
        #//Estado 1 x == True
    y = False
        #//Estado 2 y == False
    res = x and y
        #//Estado 3 res == False
    x = res and x
        #//Estado 4 x == False
    return x
    


# EJERCICIO 9:
def rt (x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

#9.1) Si evaluo tres veces seguidas ro(1) == 2 
#                                   ro(1) == 3 
#                                   ro(1) == 4

#9.2) Si evaluo tres veces seguidas rt(1,0) == 2

#9.3)
#RT:
#PRIMERA LLAMADA:
#//Estado 1 x == 1 
#//Estado 2 g == 0
#//Estado 3 g == g + 1 == 0 + 1 == 1
#//Estadp 4 return == x + g == 1 + 1 == 2
#SEGUNDA LLAMADA:
#//Estado 1 x == 1 
#//Estado 2 g == 0
#//Estado 3 g == g + 1 == 0 + 1 == 1
#//Estadp 4 return == x + g == 1 + 1 == 2
#TERCERA LLAMADA:
#//Estado 1 x == 1 
#//Estado 2 g == 0
#//Estado 3 g == g + 1 == 0 + 1 == 1
#//Estadp 4 return == x + g == 1 + 1 == 2

#R0:
#PRIMERA LLAMADA:
#//Estado 1 x == 1
#//Estado 2 g == 0
#//Estado 3 g == g + 1 == 0 + 1 == 1
#//Estado 4 return == x + g == 1 + 1 == 2
#SEGUNDA LLAMADA:
#//Estado 1 x == 1
#//Estado 2 g == 1
#//Estado 3 g == g + 1 == 1 + 1 == 2
#//Estado 4 return == x + g == 1 + 2 == 3
#TERCERA LLAMADA:
#//Estado 1 x == 1
#//Estado 2 g == 2
#//Estado 3 g == g + 1 == 2 + 1 == 3
#//Estado 4 return == x + g == 1 + 3 == 4

#9.4)
#problema ro (in int: x):int {
#requiere: {True}
#requiere: {g es una variableGlobal g: int = 0}
#asegura: {res = x + (g+1)}

#problema rt (in int: x, inout int: g):int {
#requiere: {True}
#asegura: {res = x + (g+1)}