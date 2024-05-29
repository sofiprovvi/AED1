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
#con for:
def vocales (palabra: str) -> bool:
    cantidad_vocales: int = 0
    mas_de_tres_vocales: bool = False
    
    for letra in palabra:
        if (letra =='a') or (letra =='e') or (letra =='i') or (letra == 'o') or (letra == 'u'): 
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
        if (palabra[i] =='a') or (palabra[i]=='e') or (palabra[i] =='i') or (palabra[i] == 'o') or (palabra[i] == 'u'): 
            cantidad_vocales += 1
        i+=1

    if cantidad_vocales >= 3: 
          mas_de_tres_vocales = True

    return mas_de_tres_vocales



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
        if char in 'aeiouAEIOU': 
            nueva_palabra += ['_']
        elif (char !='a') and (char !='e') and (char !='i') and (char != 'o') and (char != 'u'): 
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
        if (char =='a') or (char =='e') or (char =='i') or (char == 'o') or (char == 'u'): 
            nueva_palabra = nueva_palabra
        elif (char !='a') and (char !='e') and (char !='i') and (char != 'o') and (char != 'u'): 
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
        if palabra[i] not in palabrita:
           palabrita += palabra[i]
    return palabrita                           

palabra4: str = "odontología"
print("eliminar_repetidos:")
print("--antes: " + palabra4)
print("--da_vuelta_str: " + str(eliminar_repetidos(palabra4)))
print("--después: " + palabra4)