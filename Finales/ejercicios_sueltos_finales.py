#EJERCICIO 1:
def nuevaMatriz (sumar: list[int], m:list[list[int]]) -> list[list[int]]:
    resultado: list[list[int]] = []
    fila: list[int] = []
    i:int=0
    e:int=0

    for f in m:
        while i<len(sumar):
              e+= f[i] + sumar[i]
              fila.append(e)
              i+=1
              e=0
        resultado.append(fila)
        fila=[]
        i=0
        e=0

    return resultado          


m = [[1,4,3,2],
     [6,1,8,9],
     [2,9,7,4],
     [3,2,3,3]
     ]

s = [3,2,8,4]

print(nuevaMatriz(s,m))





#EJERCICIO 2:
def esDamero (m:list[list[int]]) -> bool:
    i:int=0
    c:int=0
    columna:list[int]=[]
    for fila in m:
         if len(fila)==8:
            while (i+1) < len(fila):
                  if fila[i]==1:
                     if fila[i+1]==0:
                        res=True
                     else:
                        res=False
                        break
                  elif fila[i]==0 :
                     if fila[i+1]==1:
                        res=True
                     else:
                        res=False
                        break 
                  i+=1
         else:
             res=False
             break
         i=0
    while c<8:  
        for fila in m:
            columna.append(fila[c])
        if len(columna)==8:
           while (i+1) < len(columna):
                  if columna[i]==1:
                     if columna[i+1]==0:
                        res=True
                     else:
                        res=False
                        break
                  elif columna[i]==0 :
                     if fila[i+1]==1:
                        res=True
                     else:
                        res=False
                        break 
                  i+=1
        else:
             res=False 
             break    
        columna=[]
        c+=1
        i=0

    return res    
                                      
                        
tablero = [[1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1]
]

falso_tablero = [[0,1,0],
                 [1,0,1],
                 [0,1,0]
                 ]

print(esDamero(tablero))
print(esDamero(falso_tablero))