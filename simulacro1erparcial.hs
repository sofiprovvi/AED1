--SIMULACRO PRIMER PARCIAL:

--EJERCICIO 1: 
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:[]) =True
relacionesValidas (x:y:[]) | (tuplasNoIguales x) && (tuplasNoIguales y) && (tuplasNoRepetidas x y) =True
relacionesValidas (x:y:xs) | (tuplasNoIguales x) && (tuplasNoIguales y) && (tuplasNoRepetidas x y) && relacionesValidas (x:xs) && relacionesValidas (y:xs) =True
                           | otherwise =False


tuplasNoIguales :: (String, String) -> Bool
tuplasNoIguales v | fst v == snd v =False
                  | otherwise =True

tuplasNoRepetidas :: (String, String) -> (String, String) -> Bool 
tuplasNoRepetidas v w | (fst v == snd w) && (snd v == fst w) =False 
                      | (fst v == fst w) && (snd v == snd w) =False
                      | otherwise =True   



--EJERCICIO 2:
personas :: [(String, String)] -> [String]
personas (x:[]) = [fst x] ++ [snd x]
personas (x:xs) = eliminarRepetidos ([fst x] ++ [snd x] ++ personas (xs))


eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x (xs) = eliminarRepetidos (quitarTodos x (xs))
                         | otherwise = [x] ++ eliminarRepetidos (xs)  
                          

quitarTodos :: String -> [String] -> [String]
quitarTodos n (x:[]) | n==x =[]
                     | n/=x = [x]
quitarTodos n (x:xs) | n==x = quitarTodos n (xs)
                     | otherwise = [x] ++ quitarTodos n (xs)
                
pertenece :: String -> [String] -> Bool
pertenece _ [] =False
pertenece [] _ =False
pertenece n (x:xs) | n==x =True
                   | n/=x =pertenece n (xs)

--si quiero que devuelva una lista de elementos de una lista de tuplas sin que se repitan:
--1) paso la lista de tuplas a lista de elementos.
--2) a esa lista de elementos le elimino los repetidos 
--3) para la función eliminar repetidos: hago funciom quitarTodos y pertenece



--EJERCICIO 3:
amigosDe :: String -> [(String, String)] -> [String]
amigosDe p [] = []
amigosDe p [x] | perteneceATupla p x && perteneceAElemento1 p x = [snd x]
               | perteneceATupla p x && perteneceAElemento2 p x = [fst x]  
               | noperteneceATupla p x =[]
amigosDe p (x:xs) | perteneceATupla p x && perteneceAElemento1 p x = [snd x] ++ amigosDe p (xs)
                  | perteneceATupla p x && perteneceAElemento2 p x = [fst x] ++ amigosDe p (xs)
                  | noperteneceATupla p x = amigosDe p (xs)
                   

perteneceATupla :: String -> (String, String) -> Bool
perteneceATupla p v | p== fst v || p== snd v =True
                    | otherwise =False

noperteneceATupla :: String -> (String, String) -> Bool
noperteneceATupla p v | p== fst v || p== snd v =False
                      | otherwise =True

perteneceAElemento1 :: String -> (String, String) -> Bool
perteneceAElemento1 p v | p== fst v =True
                        | otherwise =False

perteneceAElemento2 :: String -> (String, String) -> Bool
perteneceAElemento2 p v | p== snd v =True
                        | otherwise =False



--EJERCICIO 4:
personasConMasAmigos :: [(String, String)] -> String
personasConMasAmigos (x:xs) = masRepetido (listaElementos (x:xs))

masRepetido :: [String] -> String
masRepetido (x:[]) = x
masRepetido (x:y:xs) | cantidadDeApariciones  x (x:y:xs) >= cantidadDeApariciones y (x:y:xs) = masRepetido (x:xs)
                     | cantidadDeApariciones  x (x:y:xs) <= cantidadDeApariciones y (x:y:xs) = masRepetido (y:xs)

cantidadDeApariciones :: String -> [String] -> Int
cantidadDeApariciones p [] = 0
cantidadDeApariciones p (x:[]) | p==x =1
                               | p/=x =0
cantidadDeApariciones p (x:xs) | p==x = 1 + cantidadDeApariciones p (xs)
                               | p/=x = cantidadDeApariciones p (xs)

listaElementos :: [(String, String)] -> [String]
listaElementos (x:[]) = [fst x] ++ [snd x]
listaElementos (x:xs) = [fst x] ++ [snd x] ++ listaElementos (xs)

--si quiero saber cuál es el más repetido de una tupla:
--1) paso la tupla a lista de elementos
--2) calculo el elemento más repetido de una cadena de elementos
--3) calculo la cantidad de apariciones de un elemento en una lista