def nuevaSecuencia (s: list[int], t: list[int]) -> list[int]:
    res: list[int] = []
    maximo: int = 0
    subsecuencia: list[int] = []
    e: int = 0
    for i in range (0,len(s),1):
        if s[i] <= len(t):
            for n in range (0,s[i]+1,1):
                subsecuencia.append(t[n])
            print(subsecuencia)    
            while e < len(subsecuencia):
                 if subsecuencia[e] > maximo:
                     maximo = subsecuencia[e]
                 e+=1
            res.append(maximo)
            maximo = 0
            e=0
            subsecuencia = []
        else:
            res.append(t[len(t)-1])    
    return res                     
                         
s=[4,3,2,1,7]
t=[1,2,3,4,5]
#resultado esperado = [5,4,3,2,5]
print(nuevaSecuencia(s,t))