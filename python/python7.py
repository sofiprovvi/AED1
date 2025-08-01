import math

#PRIMERA PARTE:

#Ejercicio 1:

#1.1)
def pertenece (s: list[int], e: int)-> bool:
    lo_encontre: bool = False
    for x in s:
        if x == e:
           lo_encontre = True
    return lo_encontre

print("pertenece")
print(pertenece([2,3,4,5],6))


def pertenece_2 (s: list [int], e:int) -> bool:
    lo_encontre: bool = False
    i: int = 0
    while i < len(s) and not lo_encontre:
       if e == s[i]:
           lo_encontre = True
       i +=1

    return lo_encontre       

print("pertenece_2")
print(pertenece_2([2,3,4,5,6,7,8,2,3],7))


#1.2)
#con for:
def divide_a_todos (s: list[int], e:int) -> bool:
    lo_divide: bool = False
    for i in s:
        if math.ceil((i/e)) == (i/e):
           lo_divide = True
    return lo_divide 


#con while:
def divide_a_todos2 (s: list[int], e:int) -> bool:
    lo_divide: bool = False
    i: int = 0
    while i<len(s) and not (lo_divide):
        if math.ceil((s[i]/e)) == (s[i]/e):
           lo_divide = True
        i+=1   
    return lo_divide 
      

#1.3)
#con for:
def suma_total (s: list[int]) -> int:
    suma: int = 0
    for i in s: 
        suma += i  
    return suma  

#con while:
def suma_total2 (s: list[int]) -> int:
    suma: int = 0
    i: int = 0
    while i<len(s):
          suma += s[i]
          i+=1
    return suma  
     

#1.4)
#con for:
def ordenados (s: list[int]) -> bool:
    esta_ordenado = True
    for i in range(0,len(s)-1,1):
        if s[i]> s[i+1]: 
            esta_ordenado = False
    return esta_ordenado 

#con while:
def ordenados2 (s: list[int]) -> bool:
    esta_ordenado: bool = True
    i: int = 0
    while i<(len(s)-1) and (esta_ordenado):
          if s[i]> s[i+1]:
             esta_ordenado = False
          i+=1
    return esta_ordenado  


#1.5)
#con for:
def longitud7 (s: list[str]) -> bool:
    mayor_a_7: bool = False
    for i in s:
        if (len(i))>=7:
           mayor_a_7 = True
    return mayor_a_7        

#con while:
def longitud72 (s: list[str]) -> bool:
    mayor_a_7: bool = False
    i: int = 0
    while i<(len(s)) and not (mayor_a_7):
        if len(s[i])>=7:
           mayor_a_7 = True
        i+=1   
    return mayor_a_7


#1.6)
#con for:
def palindromo (s: str) -> bool:
    es_palindromo: bool = True
    for i in range (0,len(s)-1,1):
        if s[i]!=s[(len(s)-i-1)]:
           es_palindromo = False
    return es_palindromo        

#con while:
def palindromo2 (s: str) -> bool:
    es_palindromo: bool = True
    i = 0
    while i<len(s)-1 and es_palindromo:
        if s[i]!=s[(len(s)-i-1)]:
           es_palindromo = False
        i+=1   
    return es_palindromo


#1.7)
def fortaleza(contrasena: str)-> str:
    tiene_numeros: bool = False
    tiene_min: bool = False
    tiene_may: bool = False

    for letra in contrasena:
       if '0' <= letra and letra <= '9': #por el código ASCII
           tiene_numeros =True
       if 'a' <= letra and letra <= 'z':
           tiene_min =True
       if 'A' <= letra and letra <= 'Z':
           tiene_may =True        

    if len(contrasena)>8 and tiene_may and tiene_min and tiene_numeros:
        fort = "VERDE"
    elif len(contrasena)<5:
        fort = "ROJO"
    else:
        fort = "AMARILLO"
    return fort    


print("FORTALEZA:") 
print(fortaleza("opas"))
print("fortaleza") 
print(fortaleza("opassssssss"))
print("fortaleza") 
print (fortaleza("Opas2382347329"))


#1.8)
def saldo (movimientos: list[tuple [str, int]]) -> int:
    dinero: int = 0
    for movimiento in movimientos:

        if movimiento[0] == "I":
           dinero += movimiento[1]
        else:
           dinero -= movimiento[1]    

    return dinero    

print ("saldo: " + str(saldo([("I",1000),("R",100)])))


#1.9)
def perteneceC (s: list[chr], char: chr)-> bool:
    lo_encontre: bool = False
    for x in s:
        if x == char:
           lo_encontre = True
    return lo_encontre

#con for:
def vocales (palabra: str) -> bool:
    cantidad_vocales: int = 0
    mas_de_tres_vocales: bool = False
    
    for letra in palabra:
        if perteneceC("aeiouAEIOU", letra): 
            cantidad_vocales += 1

    if cantidad_vocales >= 3: 
          mas_de_tres_vocales = True

    return mas_de_tres_vocales

#con while:
def vocales2 (palabra: str) -> bool:
    cantidad_vocales: int = 0
    mas_de_tres_vocales: bool = False
    i: int = 0

    while i < len(palabra):
        if perteneceC("aeiouAEIOU", palabra[i]): 
            cantidad_vocales += 1
        i+=1

    if cantidad_vocales >= 3: 
          mas_de_tres_vocales = True

    return mas_de_tres_vocales


#SEGUNDA PARTE:

#Ejercicio 2:

#2.1)
def quitarPares1 (numeros: list [int]) -> list[int]:
    for i in range(0,len(numeros)-1,1):
        if numeros[i]%2==0:
            numeros[i]=0
        else:
            numeros[i]=numeros[i]   
    return numeros         

enteros1: list = [1,2,3,4,5,6,7]
print("quitarPares1:")
print("--antes: " + str(enteros1))
quitarPares1(enteros1)
print("--después: " + str(enteros1))


#2.2)
def quitarPares2 (numeros: list [int]) -> list[int]:
    reemplazar_por_cero: list[int] = []
    for n in numeros:
        if n%2==0:
            reemplazar_por_cero=[0]
        else:
            reemplazar_por_cero=[n]  
    return reemplazar_por_cero 

enteros2: list = [1,2,3,4,5,6,7]
print("quitarPares2:")
print("--antes: " + str(enteros2))
quitarPares2(enteros2)
print("--después: " + str(enteros2))


#2.4)
def elimina_vocales1 (palabra: list[chr]) -> list[chr]:
    nueva_palabra: list[chr] = []
    for char in palabra:
        if perteneceC("aeiouAEIOU", char): 
            nueva_palabra += ['_']
        elif not perteneceC("aeiouAEIOU", char): 
            nueva_palabra += char
    return nueva_palabra           

palabra1: str = "taylor swift"
print("elimina_vocales1")
print("--antes: " + palabra1)
print("--elimina_vocales: " + str(elimina_vocales1 (palabra1)))
print("--después: " + palabra1)


#2.3)
def elimina_vocales2 (palabra: list[chr]) -> list[chr]:
    nueva_palabra: list[chr] = []
    for char in palabra:
        if perteneceC("aeiouAEIOU", char): 
            nueva_palabra = nueva_palabra
        elif not perteneceC("aeiouAEIOU", char): 
            nueva_palabra += char
    return nueva_palabra        

palabra2: list[chr] = "taylor swift"
print("elimina_vocales2")
print("--antes: " + palabra2)
elimina_vocales2 (palabra2)
print("--después: " + palabra2)


#2.5)
def da_vuelta_str (palabra: list [chr]) -> list[chr]:
    al_reves: list[chr] = []
    for i in range(0,len(palabra)-1,1):
        al_reves += [palabra[len(palabra)-i-1]] 
    return al_reves + [palabra[0]]

palabra3: str = "roma"
print("da_vuelta_str:")
print("--antes: " + palabra3)
print("--da_vuelta_str: " + str(da_vuelta_str(palabra3)))
print("--después: " + palabra3)



#2.6)
def eliminar_repetidos (palabra: list[chr]) -> list[chr]:
    palabrita = []
    sin_repetir: list[chr] = []
    for i in range(0,len(palabra)-1,1):
        if not perteneceC(palabrita, palabra[i]):
           palabrita += palabra[i]
    return palabrita                           

palabra4: str = "odontología"
print("eliminar_repetidos:")
print("--antes: " + palabra4)
print("--da_vuelta_str: " + str(eliminar_repetidos(palabra4)))
print("--después: " + palabra4)


#Ejercicio 3:
def aprobado (notas: list[int]) -> int:
    suma: int = 0
    for n in notas:
       suma += n  
    promedio: int = math.ceil(suma/(len(notas)))
    caso1: bool = False
    caso2: bool = False
    caso3: bool = False
    for i in range (0,len(notas)-1,1):
          if (notas[i]) >= 4 and (promedio>=7):
            caso1 = True 
          elif (notas[i]) >= 4 and (promedio>4 and promedio<=7):
            caso2 = True   
          elif not (caso1) and not (caso2) and (notas[i]<4 or promedio<4): 
            caso3 = True
    if caso1:
       res = 1
    elif caso2:
       res = 2
    elif caso3:
       res = 3                                  
    return res
                      
                      
#Ejercicio 4:                     
 
#4.1)
def obtener_estudiantes () -> list[str]:
    estudiantes = []
    while(True):
         estudiante = str(input("Ingresa los nombres de los estudiantes ('listo' para terminar): "))
         if(estudiante=="listo"):
            break
         estudiantes += [estudiante]               
    return estudiantes


#4.2)
def monedero () -> list[tuple[str, int]]:
    historial: list[tuple[str, int]] = [] 
    credito_final: int = 0
    while(True):
        operacion = str(input("Ingrese operación: "))
        if operacion == "C" or operacion == "D":
                monto = int(input("Ingrese monto: "))
                historial += [(operacion,monto)]
        elif operacion == "X":
                break
        if operacion == "C":
            credito_final += monto
        elif operacion == "D":
            credito_final -= monto
    print(credito_final)                    
    return historial  


#4.3)
import random

def siete_y_medio () -> list[int]:
    suma: float = 0
    cartas: list[int] = []
    aleatorio: int = random.randint(0,12)   
    while aleatorio == 8  or aleatorio == 9: 
        aleatorio = random.randint(0,12)
    while(True):
           print("Su carta es: " + str(aleatorio))
           cartas += [aleatorio]    
           respuesta = str(input("Si desea seguir sacando otra carta, conteste 'si'. De lo contrario, conteste 'no': "))
           if respuesta == "si": 
                if aleatorio == 10 or aleatorio == 11 or aleatorio == 12:
                   suma += 0.5
                else:
                   suma += aleatorio 
           if respuesta == "no":
                break    
    if suma > 7.5:
          print("Perdiste")
    else: print("Ganaste")
    return cartas    
                                    
                     
                 
#Ejercicio 5:

#5.1)                        
def pertenece_a_cada_uno_version_1 (enteros: list[list[int]], e: int, res: list[bool]):
    for lista in enteros:
        if pertenece (lista,e):
            res += [True]
        else:
            res += [False]   
             
version1r = [False,False]    
version1 = [[6,5,4,3],[1,2,3,5,6,7],[9,7,8],[3]] 
print("pertenece_a_cada_uno_version_1:")
print("ANTES: ")
print("--version1: " + str(version1))
print("--version1r: " + str(version1r))
pertenece_a_cada_uno_version_1(version1,7,version1r)
print("DESPUÉS: ")
print("--version1: " + str(version1))
print("--version1r: " + str(version1r))  

                  
#5.2)                       
def pertenece_a_cada_uno_version_2 (enteros: list[list[int]], e: int, res: list[bool]):
    res.clear() #pongo res.clear() porque me limpia el res q yo tengo como parámetro. 
                #res = [] le asignaría un nuevo valor a res, 
                #sin modificar el valor de mi parámetro. 
    for lista in enteros:
        if pertenece (lista,e):
            res += [True]
        else:
            res += [False]                 
              
print("pertenece_a_cada_uno_version_2:")
print("ANTES: ")
print("--version2: " + str(version1))
print("--version2r: " + str(version1r))
pertenece_a_cada_uno_version_2(version1,7,version1r)
print("DESPUÉS: ")
print("--version2: " + str(version1))
print("--version2r: " + str(version1r)) 


#5.3)
def es_matriz (s: list[list[int]]) -> bool:
    es_matriz_wtf: bool = False
    i: int = 0
    while i<len(s)-1 and not (es_matriz_wtf):
        if len(s[i])==len(s[0]):
           es_matriz_wtf = True
        i+=1   

    return es_matriz_wtf
   

#5.4)         
def filas_ordenadas (m: list[list[int]],res: list[bool]):
    res.clear()
    i: int = 0
    while i<len(m):
        if ordenados (m[i]):
            res += [True]
        else:
            res += [False] 
        i+=1       

matriz = [[6,5,4,3],[1,2,3,5],[9,7,8,3]] 
print("filas_ordenadas:")
print("ANTES: ")
print("--matriz: " + str(matriz))
print("--version1r: " + str(version1r))
filas_ordenadas(matriz,version1r)
print("DESPUÉS: ")
print("--matriz: " + str(matriz))
print("--version1r: " + str(version1r))             


#5.5)
import numpy as np

def multiplicar_matriz (d: int,p: int) -> list[list[int]]:
    m = np.random.randint(0,2, (d,d))
    res = m**p
    return res
