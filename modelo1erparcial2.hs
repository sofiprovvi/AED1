--MODELO 1ER PARCIAL 2:


--EJERCICIO 1:

atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes (x:xs) (y:ys) n = n - sumaGoles (y:ys)

sumaGoles :: [Int] -> Int
sumaGoles [x] = x
sumaGoles (x:y:[]) = x+y
sumaGoles (x:xs) = x + sumaGoles (xs)



--EJERCICIO 2:

equiposValidos :: [(String, String)] -> Bool
equiposValidos (x:xs) = hayRepetidos (listaElementos (x:xs))

listaElementos :: [(String, String)] -> [String]
listaElementos [] = []
listaElementos [x] = [fst x] ++ [snd x]
listaElementos (x:xs) = [fst x] ++ [snd x] ++ listaElementos (xs)

hayRepetidos :: [String] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:y:[]) | x==y =False
                      | otherwise =True
hayRepetidos (x:xs) | pertenece x (xs) =True
                    | otherwise = hayRepetidos (xs)

pertenece :: String -> [String] -> Bool
pertenece s [] =False
pertenece s (x:xs) | s==x =True
                   | otherwise = pertenece s (xs)



--EJERCICIO 3:

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles s (x:xs) (y:ys) = division (devuelveElemento s (x:xs) (y:ys)) (sumaGoles (y:ys))

devuelveElemento :: String -> [(String, String)] -> [Int] -> Int
devuelveElemento s [x] [n]| s== snd x =n
devuelveElemento s (x:y:[]) (n:m:[]) | s==snd x =n
                                     | s==snd y =m
devuelveElemento s (x:xs) (n:ns) | s==snd x =n
                                 | otherwise = devuelveElemento s (xs) (ns)


division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b



--EJERCICIO 4:
vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida [x] [n] = snd x
vallaMenosVencida (x:y:[]) (n:m:[]) | n>=m =snd y
                                    | n<m =snd x
vallaMenosVencida (x:y:xs) (n:m:ns) | n>=m =vallaMenosVencida (y:xs) (m:ns)
                                    | n<m =vallaMenosVencida (x:xs) (n:ns)