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


def pertenece_2 (s: list[int], e:int) -> bool:
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
    esta_ordenado: bool = False
    for i in range(0,len(s)-1,1):
        if s[i]<= s[i+1]:
           esta_ordenado = True
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
    while i<len(s) and not (mayor_a_7):
        if len(s[i])>=7:
           mayor_a_7 = True
        i+=1   
    return mayor_a_7



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


print("fortaleza") 
print(fortaleza("opas"))
print("fortaleza") 
print(fortaleza("opassssssss"))
print("fortaleza") 
print (fortaleza("Opas2382347329"))

