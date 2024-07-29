from queue import Queue as Cola

# Ejercicio 1:
def quitar_jugador_estrategias(estrategias: dict[str,str],clave:str) -> dict[str,str]:
    dic: dict[str,str] ={}
    for jugador,estrategia in estrategias.items():
        if not clave in jugador:
           dic[jugador]=estrategia
    return dic 


def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    res: dict[str,int]={}
    for jugador,estrategia in estrategias.items():
          p:int=0
          dicc = quitar_jugador_estrategias(estrategias,jugador)   
          if estrategias[jugador]=='me desvio siempre':
           for j,e in dicc.items():    
                if dicc[j] =='me desvio siempre':
                   p+=-10 
                elif dicc[j] =='me la banco y no me desvio':   
                   p+=-15  
          if estrategias[jugador]=='me la banco y no me desvio':
           for j,e in dicc.items():     
                if dicc[j] =='me desvio siempre':
                   p+=-10 
                elif dicc[j] =='me la banco y no me desvio':   
                   p+=-5 
          if not jugador in res.keys():
             res[jugador]=p

    return res             





# Ejercicio 2:
def generar_cola (fila_clientes: list[tuple[str,str]]) -> Cola[tuple[str,str]]:
    c: Cola[tuple[str,str]] = Cola()
    for tupla in fila_clientes:
        c.put(tupla)
    return c  

def imprimir_cola (fila_clientes: Cola[str]) -> list[str]:
    lista: list[str]=[]
    while not (fila_clientes.empty()):
          g = fila_clientes.get()
          lista.append(g)
    return lista      


def reordenar_cola_priorizando_vips(fila_clientes: Cola[tuple[str,str]]) -> Cola[str]:
    c: Cola[str] = Cola()
    provisoria: list[tuple[str,str]] = []
    clientes_comunes: list[str] = []
    clientes_vip: list[str] = []
    while not (fila_clientes.empty()):
          g = fila_clientes.get()
          provisoria.append(g)     
    for p in provisoria:
        if p[1]=="vip":
           clientes_vip.append(p[0]) 
        elif p[1]=="comun":
            clientes_comunes.append(p[0])       
    for vip in clientes_vip:
        c.put(vip)
    for comun in clientes_comunes:
        c.put(comun)    
    for p in provisoria:
        fila_clientes.put(p)    
    return c





#Ejercicio 3:
def quitar_espacio (texto:str) -> str:
    letra = " "
    lista: str = []
    for c in texto:
      if letra not in c:
         lista+=c
    return lista  

def quitar_primer_caracter (texto:str) -> str:
    lista: str = []
    for i in range (1,len(texto),1):
        lista+= texto[i]
    return lista    


def son_lo_mismo (letra:chr,letra2:chr) -> bool:
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (0,len(minusculas)-1,1):
        if letra == minusculas[i] and letra2 ==minusculas[i]:
            return True
        elif letra == minusculas[i] and letra2 ==mayusculas[i]:
            return True
        elif letra == mayusculas[i] and letra2 ==mayusculas[i]:
            return True
        elif letra == mayusculas[i] and letra2 ==minusculas[i]:
            return True
    return False      

def es_palindromo (texto:str) -> bool:
    texto2 = quitar_espacio(texto)
    for i in range (0,len(texto2)-1,1):
        if len(texto2)==0:
           return False
        if len(texto2)==1:
           return True
        else:
           if son_lo_mismo (texto2[i], texto2[len(texto2)-i-1]):
             return True
           else:
             return False  
    return False   

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    i: int = 0
    while len(texto) > 0:
         if es_palindromo(texto):
             i+=1
         texto = quitar_primer_caracter (texto)  
    return i+1





# Ejercicio 4
def quien_gano_el_tateti_facilito (tablero: list[list[str]]) -> int: 
        res1: bool = False
        res2: bool = False 
        n:int=0
        i:int=0
        lista: list[str] = []
        for fila in tablero:
            lista.append(fila[n])
        while len(lista)>=3:
                if lista[i]=='X' and lista[i+1]=='X' and lista[i+2]=='X':
                    res1 = True
                if lista[i]=='O' and lista[i+1]=='O' and lista[i+2]=='0':
                    res2 = True
                i+=1    
                while n<len(fila):
                    n+=1
                    lista =[] 

        if res1 and not res2:
                  res = 1
        elif res2 and not res1:
                  res = 2
        elif not res1 and not res2:
                  res = 0
        elif res1 and res2:
                  res = 3                        

        return res


t = [['X',' ',' ',' ',' '],
     ['X',' ','O',' ',' '],
     [' ',' ','O',' ',' '],
     [' ',' ','O',' ',' '],
     [' ',' ',' ',' ',' ']
     ]
     
  