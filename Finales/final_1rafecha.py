def esSudokuValido (m: list[list[int]]) -> bool:
    f:int=0
    for fila in m:
        while f<9:
            for i in range (0,9,1):
                if (fila[f] == fila[i]) and (i!=f) and (fila[i]!=0) and (fila[f]!=0):
                    res1 = False
                else:
                    res1 = True    
            f+=1

    a: int = 0
    c: int = 0
    columna: list = []

    while c < 9:
          for fila in m:
              columna.append(fila[c])
          while a < 9:
                for e in range (0,9,1):
                    if (columna [a] == columna[e]) and (e!=a) and (columna[a]!=0) and (columna[e]!=0):
                            res2 = False
                    else: 
                            res2 = True   
                a+=1

          columna = []
          c+=1
          a=0


    if (res1 == True) and (res2 == True):
        res = True
    else:
        res = False

    return res                                                 


m = [[1,2,3,4,5,6,7,8,9],
     [9,8,7,6,4,5,3,2,1],
     [0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,4,0,0,0],
     [0,0,0,0,6,0,0,0,0],
     [0,0,0,5,0,0,0,0,0],
     [0,0,4,0,0,0,0,0,0],
     [0,3,0,0,0,0,0,0,0],
     [2,0,0,0,0,0,0,0,0]
]


print (esSudokuValido(m))