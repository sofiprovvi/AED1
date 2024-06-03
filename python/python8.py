#GUIA 8:


#EJERCICIO 1:

#1.1)
def contar_lineas (nombre_archivo:str):
   f = open(nombre_archivo)
   res = 0
   for linea in f.readlines():
       res += 1
   f.close()
   return res    

def contar_lineas2 (nombre_archivo:str):
   f = open(nombre_archivo)
   res = 0
   for linea in f.readlines():
       res += 1
   f.close()
   return res       


