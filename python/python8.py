#GUIA 8:
import math

#EJERCICIO 1:

#1.1)
def contar_lineas (nombre_archivo: str) -> int:
   f = open(nombre_archivo)
   res = 0
   for linea in f.readlines():
       res += 1
   f.close()
   return res     



#1.2) 
def pertenece (linea: list[str], palabra: str) -> bool:
    lo_encontre: bool = False
    for elemento in linea:
             if palabra == elemento:
                lo_encontre = True
    return lo_encontre                                   

def existe_palabra (palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo,"r")
    leo_archivo = archivo.readlines()
    archivo.close()
    existe: bool = False
    for renglon in leo_archivo:
        if pertenece ((separarEnPalabras(renglon)),palabra):
           existe = True
    return existe         

def separarEnPalabras (renglon: str) -> list [str]:
    temporalmente: str = "" # en esta variable voy ir armando y guardando temporalmente cada una de las palabras
    res: list [str] = []
    i: int = 0
    while i < len(renglon):
        if esUnEspacio (renglon[i]):
            res.append (temporalmente) 
            temporalmente = "" # vacio y dejo temp lista para comenzar a guardar la proxima palabra
            while i < len(renglon) and esUnEspacio(renglon[i]): # para saltearme varios espacios continuos
                i+=1
        else:
            temporalmente += renglon[i]
            i+=1
    return res

def esUnEspacio (c: str) -> bool:
    return c == " " or c == "\n" or c == "\t"



#1.3)
def cantidad_apariciones (palabra : str, nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    leo_archivo = archivo.readlines()
    i: int = 0
    for renglon in leo_archivo:
         i += (pertenece2 ((separarEnPalabras (renglon)), palabra))
    archivo.close()   
    return i        

def pertenece2 (linea: list[str], palabra: str) -> int:
    aparicion: int = 0
    for elemento in linea:
        if palabra == elemento:
                aparicion += 1
        else:
                aparicion += 0 
    return aparicion          


#EJERCICIO 2:
def clonar_sin_comentarios (nombre_archivo: str):
    archivo = open(nombre_archivo, "r+")
    nuevo_archivo = open("nuevo_archivo.txt","w")
    leo_archivo = archivo.readlines()
    nuevo_renglon: str = ""
    for renglon in leo_archivo:
         if renglon[0] == "#": 
            nuevo_renglon = ""
         else:
            nuevo_renglon = renglon  
         nuevo_archivo.writelines(nuevo_renglon)                   
    archivo.close()
                           
