#GUIA 8:


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
def pertenece (linea: list[chr], palabra: str) -> bool:
    lo_encontre: bool = False
    i: int = 0
    for texto in linea:
        while i<len(palabra) and not (lo_encontre):
             if palabra[i] == texto:
                lo_encontre = True
    return lo_encontre                                   

def existe_palabra(palabra: str, nombre_archivo: str)-> bool:
    archivo = open(nombre_archivo)
    leo_archivo = archivo.readlines()
    print(leo_archivo)
    for renglon in leo_archivo:
       if pertenece (renglon,palabra):
           return True
       else:
           return False


#1.3)
#def cantidad_apariciones (nombre_archivo : str, palabra : str) -> int:
#    f = open(nombre_archivo)
#    if existe_palabra (palabra, nombre_archivo):
        

