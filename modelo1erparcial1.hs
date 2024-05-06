--MODELO 1ER PARCIAL 1:

--EJERCICIO 1:

votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco (x:xs) (y:ys) c = c - votosValidos (y:ys) 

votosValidos :: [Int] -> Int
votosValidos (x:[])= x
votosValidos (x:y:[]) = (x + y)
votosValidos (x:xs) = x + votosValidos (xs)



--EJERCICIO 2:

formulasValidas :: [(String, String)] -> Bool 
formulasValidas (x:xs) | hayRepetidos (listaElementos (x:xs)) =False
                       | otherwise =True

listaElementos :: [(String, String)] -> [String]
listaElementos [x] = [fst x] ++ [snd x]
listaElementos (x:xs) = [fst x] ++ [snd x] ++ listaElementos (xs)

hayRepetidos :: [String] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:y:[]) | x==y =True
                      | otherwise =False
hayRepetidos (x:xs) | pertenece x (xs) =True
                    | otherwise = hayRepetidos (xs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece s [] =False
pertenece s (x:xs) | s==x =True
                   | otherwise = pertenece s (xs) 


--EJERCICIO 3:

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos s (x:xs) (y:ys) = division (devuelveElemento s (x:xs) (y:ys)) (votosValidos (y:ys))

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)


devuelveElemento :: String -> [(String, String)] -> [Int] -> Int
devuelveElemento s (x:[]) (y:[]) | s==fst x =y
                                 | otherwise =0
devuelveElemento s (x:xs) (y:ys) | s==fst x =y
                                 | otherwise = devuelveElemento s (xs) (ys)      


--EJERCICIO 4:

proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente (x:[]) (y:[]) =fst x
proximoPresidente (x:y:[]) (n:m:[]) | devuelveElemento (fst x) (x:y:[]) (n:m:[]) >= devuelveElemento (fst y) (x:y:[]) (n:m:[]) =fst x
                                    | otherwise = fst y
proximoPresidente (x:y:xs) (n:m:ns) | devuelveElemento (fst x) (x:y:xs) (n:m:ns) >= devuelveElemento (fst y) (x:y:xs) (n:m:ns) =proximoPresidente (x:xs) (n:ns)
                                    | otherwise =proximoPresidente (y:xs) (m:ns)

