#GUÍA 8:

from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

#PILAS:

#Ejercicio 8:
def generar_nros_al_azar (cantidad : int, desde : int, hasta : int) -> Pila[int]:
    p: Pila[int] = Pila()
    i:int=1
    while i <= cantidad:
      n: int = random.randint(desde,hasta)
      p.put(n) 
      i+=1
    return p   

def imprimir_pila (p: Pila[int]) -> list[int]:
   lista: list[int] = []
   pila: list[int] = []

   while not (p.empty()):
     g = p.get()
     pila.append(g)

   for i in range (len(pila)-1,-1,-1):
      lista.append(pila[i])

   for e in lista:
      p.put(e) 

   return lista      

print("imprimir_pila: " + str(imprimir_pila(generar_nros_al_azar(4,1,3))))



#Ejercicio 9:
def cantidad_elementos_pila(p: Pila) -> int:
   provisoria: list[int] = []
   res: list[int] = []

   while not (p.empty()):
     g = p.get()
     provisoria.append(g)

   for i in range (len(provisoria)-1,-1,-1):
      res.append(provisoria[i])

   for e in res:
      p.put(e)

   return len(res)        

print("cantidad_elementos_pila: " + str(cantidad_elementos_pila(generar_nros_al_azar(4,1,3))))



#Ejercicio 10:
def buscar_el_maximo_pila (p : Pila[int]) -> int:
   provisoria: list[int] = []
   res: list[int] = []

   while not (p.empty()):
     g = p.get()
     provisoria.append(g)

   for i in range (len(provisoria)-1,-1,-1):
      res.append(provisoria[i])

   for e in res:
      p.put(e)

   maximo = res[0]  # Asumimos que el primer elemento es el máximo
   for n in range (0,len(res)-1,1):
      if res[n]>res[0]:
         maximo = res[n]

   return maximo      
         
print("buscar_el_maximo_pila: " + str(buscar_el_maximo_pila(generar_nros_al_azar(4,1,3))))         



#Ejercicio 11:
def esta_bien_balanceada(s : str) -> bool:
    pila = Pila()
    res: bool = True

    for elemento in s:
       if elemento == "(":
          pila.put(elemento)
       elif elemento == ")":
          if pila.empty(): #si está vacia, quiere decir q antes no habia
                           # un "(", o sea no está bien balanceada 
             res = False
          else:
             pila.get()   #caso contrario, desapilo, o sea saco el "(". 
                          #entonces, si la lista final no se encuentra vacia, 
                          #va a estar mal balanceada!! 
    if not (pila.empty()):
       res = False
    return res   

print("esta_bien_balanceada: " + str(esta_bien_balanceada("10 * (1 + (2 * (-1)))")))



#Ejercicio 12:
def postfix (s : str) -> float:
    provisoria: list[str] = []
    p: Pila[int] = Pila()
    for token in s:
          if token not in "+-*/ ":
              p.put(token)
          elif token in "+-*/":
              a = float(p.get()) 
              b = float(p.get())  
              if token == '+':
                 p.put(float(b+a))  
              elif token == '-': 
                 p.put(float(b-a)) 
              elif token == '*': 
                 p.put(float(b*a)) 
              elif token == '/': 
                 p.put(float(b/a)) 
    return p.get()                     


print("postfix: " + str(postfix("3 4 + 5 * 2 -")))



#COLAS:

#Ejercicio 13:
def generar_cola (cantidad : int, desde : int, hasta : int) -> Cola[int]:
    c: Cola[int] = Cola()
    i:int=1
    while i <= cantidad:
      n: int = random.randint(desde,hasta)
      c.put(n) 
      i+=1
    return c 

def imprimir_cola (c: Cola[int]) -> list[int]:
   cola: list[int] = []

   while not (c.empty()):
     g = c.get()
     cola.append(g)

   for e in cola:
      c.put(e)  

   return cola    

print("imprimir_cola: " + str(imprimir_cola(generar_cola(4,1,3))))



#Ejercicio 14:
def cantidad_elementos_cola(c: Cola) -> int:
    cola: list[int] = []

    while not (c.empty()):
     g = c.get()
     cola.append(g)

    for e in cola:
      c.put(e)  

    print(cola)  
    return len(cola)   


print("cantidad_elementos_cola: " + str(cantidad_elementos_cola(generar_cola(4,1,3))))



#Ejercicio 15:
def buscar_el_maximo_cola (c: Cola) -> int:
    cola: list[int] = []

    while not (c.empty()):
       g = c.get()
       cola.append(g)
    print(cola)
    for e in cola:
       c.put(e) 
    
    for i in range(0,len(cola)-1,1):
        maximo = cola[0]
        if cola[i]> maximo:
            maximo = cola[i]
    return maximo        
       
print("buscar_el_maximo_cola: " + str(buscar_el_maximo_cola(generar_cola(4,1,3))))
          


#Ejercicio 16:

#16.1)
def quitar (s: list[int], e: int) -> list[int]:
    lista: list[int] = []
    for x in s:
       if x != e:
          lista.append(x)
       else: 
          lista += []    
    return lista
      
def armar_secuencia_de_bingo() -> Cola[int]:
    bolillero: list[int] = []
    i: int = 0
    while i<100:
       bolillero.append(i)
       i+=1
    c: Cola[int] = Cola

    while len(bolillero)<0:
          e: int = random.choice(bolillero)
          bolillero = quitar(bolillero,e)
          c.put(e)
    return c   

#16.2)
def jugar_carton_de_bingo (carton : list[int], bolillero : Cola[int]) -> int:
   cantSinMarcar: int = len (carton) #cantidad de fichas q tdv no coincidieron con lo q saqué del bolillero
   temp: list [int] = [] #lista temporal en donde voy a poner los elementos q saqué del bolillero, para volver a incorporarlos al final!!

   while cantSinMarcar > 0: # no hace falta ver si bolillero está vacío
        bolilla: int = bolillero.get()
        temp.append(bolilla) #voy almacenando acá los elementos que saco de bolillero
        if bolilla in carton: 
            cantSinMarcar -=1 #si lo q saqué del bolillero estaba en el cartón, me quedan menos elementos de carton por encontrar!

   jugadas: int = len (temp) #la cantidad d bolillas q saqué hasta ganar equivale a la cantidad de jugadas

   while not bolillero.empty(): # vacio por completo el bolillero para volver a llenarlo en el mismo orden!!
        temp.append(bolillero.get())

   for num in temp: # regenero el bolillero en el orden original
        bolillero.put(num)

   return jugadas

bolillero = armar_secuencia_de_bingo()
print(str(jugar_carton_de_bingo([20,45,21,56,87], bolillero)))
         