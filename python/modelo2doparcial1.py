#2do parcial: python:

#EJERCICIO 1:
def ap_antes_corte (c: chr , s: str) -> int:
    i:int = 0
    apariciones: int = 0 
    for letra in s:
        if letra=='v' and not i<0:
           i-=56
           if c=='v':
              apariciones+=1
        elif letra=='r' and not i<0:
           i+=350
           if c=='r':
              apariciones+=1
        elif letra=='s' and not i<0:
           i+=0
           if c=='s':
              apariciones+=1
        elif letra=='x' or i<0:
           break  

    while i<0:
       i+=56        
    return apariciones
           
                        
def verificar_transacciones (s: str) -> int:              
    res = (350 * (ap_antes_corte('r',s))) - (56 *(ap_antes_corte('v',s)))
    while res<0:
       res+=56
    return res




#EJERCICIO 2:
def el_minimo(e: float, s:list[float]) -> bool:
    for i in range(len(s)):
        if not (e <= s[i]):
           return False
    return True

def devuelvemin(s: list[float]) -> float:
    res: int = 0
    for elem in s:
        if el_minimo(elem, s):
           res = elem
    return res

def valor_minimo (s:list[tuple[float,float]]) -> float:
    minimas: list[float] = []
    for tupla in s:
        minimas.append(tupla[0])

    res = devuelvemin (minimas)  

    return res        
           



#EJERCICIO 3:
def valor_minimo3 (s:list[tuple[int,float]]) -> float:
    minimas: list[float] = []
    for tupla in s:
        minimas.append(tupla[1])
    res = devuelvemin (minimas)
    return res

def el_maximo(e: float, s: list[float]) -> bool:
    for i in range(len(s)):
        if not (e >= s[i]):
           return False
    return True

def devuelvemax(s: list[float]) -> float:
    res: int = 0
    for elem in s:
        if el_maximo(elem, s):
           res = elem
    return res

def valor_maximo3 (s:list[tuple[int,float]]) -> float:
    maximas: list[float] = []
    for tupla in s:
        maximas.append(tupla[1])
    
    res = devuelvemax(maximas)
    return res

valores_diarios = {'YPF':[(1,10),(15, 3), (31,100)],
                   'ALUA': [(1,0), (20, 50), (31,30)],
                   'GGAL': [(12, 9.1),(20, 40.5),(12,52),(30,84)],
                   'SOFIA':[(3, 560),(10,1500)]}

def valores_extremos (cotizaciones_diarias: dict[str, list[tuple[int,float]]]) -> dict[str, list[tuple[int,float]]]:
    for empresa,tupla in cotizaciones_diarias.items():
        tupla = [(valor_minimo3(tupla),valor_maximo3(tupla))]
        cotizaciones_diarias[empresa] = tupla 
    return cotizaciones_diarias    





#EJERCICIO 4:
def es_sudoku_valido (m: list[list[int]]) -> bool:
    columna0: list[int] = []
    columna1: list[int] = []
    columna2: list[int] = []
    columna3: list[int] = []
    columna4: list[int] = []
    columna5: list[int] = []
    columna6: list[int] = []
    columna7: list[int] = []
    columna8: list[int] = []

    for fila in m: #me fijo si en cada fila se repiten los numeros del 1 al 9, el 0 no importa
        for i in range(0,8,1):
            if fila[i]==fila[i+1] and fila[i]!=0 and fila[i+1]!=0:
                return False
    for fila in m: #hago una lista con cada columna
        columna0.append(fila[0])
        columna1.append(fila[1])
        columna2.append(fila[2])
        columna3.append(fila[3])
        columna4.append(fila[4])
        columna5.append(fila[5])
        columna6.append(fila[6])
        columna7.append(fila[7])
        columna8.append(fila[8])
    
    for i in range(0,8,1): #me fijo si en cada columna se repiten los numeros del 1 al 9, el 0 no importa
            if columna0[i]==columna0[i+1] and columna0[i]!=0 and columna0[i+1]!=0:
                return False
            elif columna1[i]==columna1[i+1] and columna1[i]!=0 and columna1[i+1]!=0:
                return False
            elif columna2[i]==columna2[i+1] and columna2[i]!=0 and columna2[i+1]!=0:
                return False
            elif columna3[i]==columna3[i+1] and columna3[i]!=0 and columna3[i+1]!=0:
                return False
            elif columna4[i]==columna4[i+1] and columna4[i]!=0 and columna4[i+1]!=0:
                return False
            elif columna5[i]==columna5[i+1] and columna5[i]!=0 and columna5[i+1]!=0:
                return False
            elif columna6[i]==columna6[i+1] and columna6[i]!=0 and columna6[i+1]!=0:
                return False
            elif columna7[i]==columna7[i+1] and columna7[i]!=0 and columna7[i+1]!=0:
                return False
            elif columna8[i]==columna8[i+1] and columna8[i]!=0 and columna8[i+1]!=0:
                return False
    return True   

                        

           




