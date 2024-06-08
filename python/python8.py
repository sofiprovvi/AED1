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
def armar_secuencia_de_bingo () -> Cola[int]:
    listaDeBolillas: list [int] = []
    for bolilla in range (0,100,1):
        listaDeBolillas.append(bolilla)

    random.shuffle(listaDeBolillas) # mezclamos la listaDeBolillas.

    bolillero: Cola [int] = Cola()
    for b in listaDeBolillas: # b son las bolillas que voy a meter en la cola bolillero
        bolillero.put(b)

    return bolillero 

#16.2)
def jugar_carton_de_bingo (carton: list[int], bolillero: Cola[int]) -> int:
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



#Ejercicio 17:
def generar_cola_tuplas (s: list[tuple[int,str,str]]) -> Cola[int,str,str]:
    c: Cola[int,str,str] = Cola()
    for x in s:
        c.put(x)

    return c   

def pacientes_urgentes(c : Cola[(int, str, str)]) -> int:
   urgencias: int = 0
   almacenamiento: list[tuple[int,str,str]] = []
   while not (c.empty()):
     g = c.get()
     almacenamiento.append(g)
     if g[0] == 1 or g[0] == 2 or g[0] == 3:
        urgencias += 1

   for a in almacenamiento:
      c.put(a)

   return urgencias     
   
print("pacientes_urgentes: " + str(pacientes_urgentes(generar_cola_tuplas([(1,"sofia","oido"),(5,"lopez","gimnasio"),(2,"malena","dientes"),(4,"joaco","pie")]))))    


#Ejercicio 18:
def generar_cola_clientes (clientes: list[str,int,bool,bool]) -> Cola[(str, int, bool, bool)]:
    c: Cola[(str, int, bool, bool)] = Cola()
    for cliente in clientes:
        c.put(cliente)
    return c    

atendidos = generar_cola_clientes([("sofi",1,True,False),("juli",4,False,False),("valen",8,True,True),("vicky",45,False,True)])

def implementar_atencion_clientes (c: Cola[str,int,bool,bool]) -> Cola[(str, int, bool, bool)]:
    prioridad: list[tuple[str,int,bool,bool]] = []
    preferencial: list[tuple[str,int,bool,bool]] = []
    resto: list[tuple[str,int,bool,bool]] = []
    total: list[tuple[str,int,bool,bool]] = []
    atendidos: Cola[tuple[str,int,bool,bool]]= Cola() 
    while not (c.empty()):
       g = c.get()
       if g[3]==True:
          prioridad.append(g)
       elif g[2]==True:
          preferencial.append(g)
       else:
          resto.append(g)
    total = prioridad + preferencial + resto
    for cliente in total:
       atendidos.put(cliente)
    return atendidos   

def imprimir_cola_atendidos (atendidos: Cola[tuple[str,int,bool,bool]]) -> list[tuple[str,int,bool,bool]]:
   cola: list[tuple[str,int,bool,bool]] = []
   while not (atendidos.empty()):
     g = atendidos.get()
     cola.append(g)
   for e in cola:
       atendidos.put(e)  
   return cola

print("atencion_clientes: " + str(imprimir_cola_atendidos(implementar_atencion_clientes(atendidos))))



#DICCIONARIOS:

#Ejercicio 19: APRENDERME ESTA FUNCION DE MEMORIAAAAA!!!!!
def separar_palabras(linea:str, espacio:str) -> list[str]:
    res:list[str] = []
    palabra:str = ""
    for letra in linea:
        if letra != espacio and letra != "\n":
            palabra = palabra + letra
        else:
            if len(palabra) > 0:
                res.append(palabra)
                palabra = ""
    res.append(palabra)
    return res

def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    archivo = open(nombre_archivo,"r")
    linea = archivo.read()
    res:dict[int,int] = dict()
    # a partir del texto entero, creo una lista de palabras:
    palabras:list[str] = separar_palabras(linea, " ")
    for palabra in palabras:
        clave: int = len(palabra)
        if clave in res.keys():
            res[clave] += 1
        else:
            res[clave] = 1   
       
    return res   



#Ejercicio 20:
def promedio_estudiante (nombre_archivo: str, lu: str) -> float:
    suma_notas: float = 0
    cantidad_notas: float = 0
    archivo = open(nombre_archivo, "r")
    leo_archivo = archivo.readline()
    while leo_archivo != '': #pongo ese while para q me haga readline con cada linea
     renglon = separar_palabras(leo_archivo," ")
     if renglon[0]==(lu):
       suma_notas += float(renglon[3])
       cantidad_notas += 1
     leo_archivo = archivo.readline()            
    archivo.close()
    promedio: float = suma_notas/cantidad_notas
    return promedio            

def calcular_promedio_por_estudiante (nombre_archivo_notas : str) -> dict[str, float]:
    archivo = open(nombre_archivo_notas, "r")
    leo = archivo.readlines()
    res: dict[str, float] = {}
    for linea in leo:
        renglon = separar_palabras(linea, " ")
        clave: str = renglon[0]
        if not clave in res.keys():
           res[clave] = promedio_estudiante(nombre_archivo_notas,clave)
    archivo.close()       
    return res    

              

#Ejercicio 21:         
def palabra_mas_frecuente (nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo)
    leo = archivo.read()
    lista = separar_palabras(leo, " ")
    res: dict[str,int] = {}
    for i in range(0,len(lista),1):
       clave = lista[i]
       if not clave in res.keys():
          res[clave] = cantidad_apariciones(lista,clave)
    archivo.close()

    mas_frecuente = ""
    aparece: int = 0 
    for palabra, aparicion in res.items():
        if aparicion > aparece:
           aparece = aparicion
           mas_frecuente = palabra 

    return mas_frecuente
          

def cantidad_apariciones (leo: list[str], palabra: str) -> int:
    i: int = 0
    for elemento in leo:
        if elemento in palabra:
           i+=1
    return i



#Ejercicio 22:

#22.1)
def imprimir_pila_historial (p: Pila[str]) -> list[str]:
    provisoria: list[str] = []
    final: list[str] = []

    while not (p.empty()):
          g = p.get()
          provisoria.append(g)

    for i in range (len(provisoria)-1,-1,-1):
        final.append(provisoria[i])

    for f in final:
       p.put(f) 

    return final            


def generar_pila_historial (s: list[str]) -> Pila[str]:
    p: Pila[str] = Pila()
    for x in s:
       p.put(x)
    return p           

pila1 = ["wattpad.com","substack.com","spotify.com"]
pila2 = ["netflix.com","percyjackson.com","cuevana.com"]
pila3 = ["freud.com","uniendocaminos.com"]
pila4 = ["itba.com","ciencia.com","analisis.com"]
pila5 = ["wos.com","pottermore.com"]

historiales = {'sofiprovvi': generar_pila_historial(pila1),
              'gastonboque': generar_pila_historial(pila2),
              'augustocasais':generar_pila_historial(pila3),
              'pilibasteguieta':generar_pila_historial(pila4),
              'inasrur7': generar_pila_historial(pila5)}


#22.2)
def visitar_sitio (historiales: dict[str, Pila[str]], usuario:str, sitio:str):
    if usuario in historiales.keys():
       pila: Pila[str] = historiales[usuario]
       pila.put(sitio)
       historiales[usuario] = pila
              
    else:
       nueva_pila: Pila [str] = Pila()
       nueva_pila.put(sitio)
       historiales[usuario] = nueva_pila
     
print("visitar_sitio")
print("--antes: ' '")
visitar_sitio(historiales,"julipavlov","amazonprime.com")  
print("--después: " + str(imprimir_pila_historial((historiales['julipavlov']))))

    
#22.3)
def navegar_atras (historiales: dict[str, Pila[str]], usuario:str):
   if usuario in historiales.keys():
       historial = historiales[usuario]
       actual = historial.get()
       anterior = historial.get()
       historial.put(actual)
       historial.put(anterior)
       historiales[usuario] = historial

print("navegar_atras")
print("--antes: " + str(imprimir_pila_historial((historiales['gastonboque']))))
navegar_atras(historiales,"gastonboque")  
print("--después: " + str(imprimir_pila_historial((historiales['gastonboque']))))



#Ejercicio 23: 
infoCamisa = { 'precio': 100.0 ,'cantidad' : 30}
infoVestido = { 'precio': 200.0 , 'cantidad' : 53}
infoPollera = { 'precio': 154.0, 'cantidad': 18}
infoCampera = { 'precio': 1234.0, 'cantidad' : 6}

inventario = {'camisa' : infoCamisa, 
              'vestido' : infoVestido,
              'pollera' : infoPollera,
              'campera' : infoCampera}

#23.1)
def agregar_producto (inventario: dict[str,dict[float,int]], nombre: str, precio: float, cantidad: int):
    infoNombre: dict[float,int] = {}
    if nombre not in inventario.keys():
       infoNombre['precio'] = precio
       infoNombre['cantidad'] = cantidad
       inventario[nombre] = infoNombre

print("agregar_producto")
agregar_producto(inventario,"sombrero",89.7,40)
print(inventario)       


#23.2)
def actualizar_stock (inventario: dict[str,dict[float,int]], nombre: str, cantidad: int):
    if nombre in inventario.keys():
       infoNombre: dict[float, int] = inventario[nombre] 
       infoNombre['cantidad'] = infoNombre['cantidad'] + cantidad
       inventario[nombre] = infoNombre 

print("actualizar_stock")
actualizar_stock(inventario,"camisa",10)
print(inventario)


#23.3)
def actualizar_precio (inventario: dict[str,dict[float,int]], nombre: str, precio: float):
     if nombre in inventario.keys():
       infoNombre: dict[float, int] = inventario[nombre] 
       infoNombre['precio'] = infoNombre['precio'] + precio
       inventario[nombre] = infoNombre 

print("actualizar_precio")
actualizar_precio(inventario,"camisa",10)
print(inventario)


#23.4)
def calcular_valor_inventario (inventario: dict[str,dict[float,int]]) -> float:
     dinero: float = 0
     for nombre, info in inventario.items():
         if nombre in inventario.keys():
            info = inventario[nombre]
            dinero += (info['cantidad'] * info['precio'])
     return dinero       

print("calcular_valor_inventario")
print(calcular_valor_inventario(inventario))

          

