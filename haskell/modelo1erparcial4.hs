--MODELO 1ER PARCIAL 4:

--EJERCICIO 1:
hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar c [] =False
hayQueCodificar c [x] | c==fst x =True
                      | otherwise =False
hayQueCodificar c (x:xs) | c==fst x =True
                         | otherwise =hayQueCodificar c (xs)
                         

--EJERCICIO 2:
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar c (y:ys) (x:xs) | hayQueCodificar c (x:xs) = cantidadDeApariciones c (y:ys)
                                            | not (hayQueCodificar c (x:xs)) =0

cantidadDeApariciones :: Char -> [Char] -> Int
cantidadDeApariciones c [x] | c==x =1
                            | otherwise =0
cantidadDeApariciones c (x:xs) | c==x =1 + cantidadDeApariciones c (xs)
                               | otherwise= cantidadDeApariciones c (xs)                             


--EJERCICIO 3:
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar [c] [x] | hayQueCodificar c [x] =c
laQueMasHayQueCodificar (c:d:[]) (x:y:xs) | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:[])) (x:y:xs) && cantidadDeApariciones c (c:d:[]) > cantidadDeApariciones (siguienteDistinto c (c:d:[])) (c:d:[]) =c
                                          | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:[])) (x:y:xs) && cantidadDeApariciones c (c:d:[]) < cantidadDeApariciones (siguienteDistinto c (c:d:[])) (c:d:[]) =siguienteDistinto c (c:d:[]) 
                                          | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:[])) (x:y:xs) && cantidadDeApariciones c (c:d:[]) == cantidadDeApariciones (siguienteDistinto c (c:d:[])) (c:d:[]) =c
                                          | not (hayQueCodificar c (x:y:xs)) && hayQueCodificar (siguienteDistinto c (c:d:[])) (x:y:xs) = siguienteDistinto c (c:d:[])
                                          | hayQueCodificar c (x:y:xs) && not (hayQueCodificar (siguienteDistinto c (c:d:[])) (x:y:xs)) = c
laQueMasHayQueCodificar (c:d:cs) (x:y:xs) | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:cs)) (x:y:xs) && cantidadDeApariciones c (c:d:cs) > cantidadDeApariciones (siguienteDistinto c (c:d:cs)) (c:d:cs) = laQueMasHayQueCodificar (quitar (siguienteDistinto c (c:d:cs)) (c:d:cs)) (x:y:xs) 
                                          | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:cs)) (x:y:xs) && cantidadDeApariciones c (c:d:cs) < cantidadDeApariciones (siguienteDistinto c (c:d:cs)) (c:d:cs) = laQueMasHayQueCodificar (quitar c (c:d:cs)) (x:y:xs)
                                          | hayQueCodificar c (x:y:xs) && hayQueCodificar (siguienteDistinto c (c:d:cs)) (x:y:xs) && cantidadDeApariciones c (c:d:cs) == cantidadDeApariciones (siguienteDistinto c (c:d:cs)) (c:d:cs) =laQueMasHayQueCodificar (quitar (siguienteDistinto c (c:d:cs)) (c:d:cs)) (x:y:xs) 
                                          | not (hayQueCodificar c (x:y:xs)) && hayQueCodificar (siguienteDistinto c (c:d:cs)) (x:y:xs) = laQueMasHayQueCodificar (quitar c (c:d:cs)) (x:y:xs)
                                          | hayQueCodificar c (x:y:xs) && not (hayQueCodificar (siguienteDistinto c (c:d:cs)) (x:y:xs)) = laQueMasHayQueCodificar (quitar (siguienteDistinto c (c:d:cs)) (c:d:cs)) (x:y:xs)    
                                                                      

siguienteDistinto :: Char -> [Char] -> Char
siguienteDistinto c [x] | c==x =c
siguienteDistinto c (x:y:[]) | c==x && c==y =c
                             | c==x && c/=y =y
siguienteDistinto c (x:y:xs) | c==x && c==y = siguienteDistinto c (y:xs)
                             | c/=x && c==y = siguienteDistinto c (y:xs)
                             | c==x && c/=y =y
                             | c/=x && c/=y =siguienteDistinto c (xs)                            
siguienteDistinto c (xs) =c

quitar :: Char -> [Char] -> [Char]
quitar c [x] | c==x =[]
             | otherwise =[x] 
quitar c (x:xs) | c==x =xs
                | c/=x = [x] ++ quitar c (xs) 
quitar c [] =[c]                




--EJERCICIO 4:
--si el elemento i de frase me da false en hayQueCodificar: res= [elemento i]
--si el elemento i de frase me da true en hayQueCodificar , 
--entonces: res = al elemento snd j de mapeo, 
-- un j tal que el fst j sea el elemento i de la frase

codificar :: [Char] -> [(Char, Char)] -> [Char]
codificar (y:ys) (x:xs) = devuelveLista2doTupla (y:ys) (x:xs)

devuelve2doTupla :: Char -> [(Char, Char)] -> [Char]
devuelve2doTupla y (x:xs) | pertenece y (lista1raTupla (x:xs)) && y== fst x =[snd x]
                          | pertenece y (lista1raTupla (x:xs)) && y/= fst x = devuelve2doTupla y (xs)
                          | not (pertenece y (lista1raTupla (x:xs))) = [y]

lista1raTupla :: [(Char, Char)] -> [Char]
lista1raTupla (x:[]) = [fst x]
lista1raTupla (x:xs) = [fst x] ++ lista1raTupla (xs)       

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece c [] =False
pertenece c (x:xs) | c==x =True
                   | otherwise = pertenece c (xs)

devuelveLista2doTupla :: [Char] -> [(Char, Char)] -> [Char]
devuelveLista2doTupla (y:[]) (x:xs) = devuelve2doTupla y (x:xs)
devuelveLista2doTupla (y:ys) (x:xs) = devuelve2doTupla y (x:xs) ++ devuelveLista2doTupla (ys) (x:xs)