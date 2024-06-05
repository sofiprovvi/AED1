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
    i: int = 0
    for texto in linea:
        while i<len(palabra) and not False:
             if palabra[i] == texto:
                return True
             else:
                 return False                                   

def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo)
    leo_archivo = archivo.readlines()
    archivo.close()
    for renglon in leo_archivo:
       if pertenece (renglon,palabra):
           return True
       else:
           return False
       


#1.3)
#def cantidad_apariciones (nombre_archivo : str, palabra : str) -> int:
 

