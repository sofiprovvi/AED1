#GUIA 8:
import math
import array

#ARCHIVOS:

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
         if es_comentario (renglon): 
            nuevo_renglon = ""
         else:
            nuevo_renglon = renglon  
         nuevo_archivo.writelines(nuevo_renglon)                   
    archivo.close()
                           
def es_comentario(linea) -> bool:
    # Inicializamos un índice para recorrer la línea
    i = 0
    # Recorremos la línea mientras haya espacios al principio
    while i < len(linea) and linea[i] == ' ':
        i += 1
    # Verificamos si el primer carácter no espacial es un '#'
    if i < len(linea) and linea[i] == '#':
        return True
    else:
        return False   
          
          

#EJERCICIO 3:
def invertir_lineas (nombre_archivo: str):
    archivo = open(nombre_archivo, "r+")
    nuevo_archivo = open("nuevo_archivo.txt","w")
    leo_archivo = archivo.readlines()
    nuevo_renglon: list[str] = ""
    for i in range (len(leo_archivo)-1,-1,-1):
       nuevo_renglon = leo_archivo[i] 
       nuevo_archivo.writelines(nuevo_renglon)                  
    archivo.close()



#EJERCICIO 4:
def agregar_frase_al_final(nombre_archivo : str, frase : str):
    archivo = open(nombre_archivo, "a")
    archivo.write("\n" + frase)
    archivo.close()



#EJERCICIO 5:
def agregar_frase_al_principio(nombre_archivo : str, frase : str):
    archivo = open(nombre_archivo, "r+")
    archivo.write("\n" + frase)
    lista: list[str] = archivo.readlines()
    archivo.close()

    archivo = open(nombre_archivo, "r+")
    lista2: list[str] = [frase + "\n"]
    for linea in lista:
        lista2 += linea

    archivo.writelines(lista2)
    archivo.close()



#EJERCICIO 6:
def listar_palabras_de_archivo (nombre_archivo : str) -> list:
    archivo = open(nombre_archivo, "r+b")
    leo_archivo = archivo.read()
    lista = []
    palabra: str = ''
    for renglon in leo_archivo:
            c = chr(renglon)
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9') or (c in '_'):
                palabra+=c
            elif len(palabra)<5:
                palabra = ''
            else:            
                lista += palabra
                palabra = ''                        
    archivo.close()            
    return lista   



#EJERCICIO 7:
def promedio_estudiante (nombre_archivo:str, lu : str) -> float:
    suma_notas: float = 0
    cantidad_notas: float = 0
    archivo = open(nombre_archivo, "r")
    leo_archivo = archivo.readline()
    while leo_archivo != '': #pongo ese while para q me haga readline con cada linea
     renglon = separarEnPalabras(leo_archivo)
     if renglon[0]==(lu):
       suma_notas += float(renglon[3])
       cantidad_notas += 1
     leo_archivo = archivo.readline()            
    archivo.close()
    promedio: float = suma_notas/cantidad_notas
    return promedio            

def calcular_promedio_por_estudiante (nombre_archivo_notas: str, nombre_archivo_promedios: str):
    notas = open(nombre_archivo_notas, "r")
    promedios = open(nombre_archivo_promedios, "w")
    notas_linea = notas.readline()
    lista: str = []
    while notas_linea != '':
        lista_notas_linea = separarEnPalabras(notas_linea)
        lu = lista_notas_linea[0]
        if not (lu in lista):
            lista += lu
            promedios.write(lu + " " + str(promedio_estudiante(nombre_archivo_notas,lu)) + "\n")  
        notas_linea = notas.readline()
    notas.close()
    promedios.close()
            
def quitarComa (elemento: str) -> str:
    palabra = ""
    for i in range (0,len(elemento)-1,1):
        if elemento[i]!=",":
            palabra += elemento[i]
        else:
            palabra += ''
    return palabra            

