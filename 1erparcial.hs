module SolucionT2 where

--EJERCICIO 1:
generarStock :: [[Char]] -> [([Char],Int)]
generarStock [x] = [(x , cantidadDeApariciones x [x])] 
generarStock (x:xs) = eliminarRepetidos ([(x, cantidadDeApariciones x (x:xs))] ++ generarStock (xs))

cantidadDeApariciones :: [Char] -> [[Char]] -> Int
cantidadDeApariciones c [x] | c==x  =1
                            | otherwise =0
cantidadDeApariciones c (x:xs) | c==x =1 + cantidadDeApariciones c (xs)
                               | c/=x = cantidadDeApariciones c (xs)

eliminarRepetidos :: [([Char],Int)] -> [([Char],Int)]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:y:[]) | x==y =[x]
                           | otherwise =[x]++[y]
eliminarRepetidos (x:y:xs) | x==y = eliminarRepetidos (y:xs)   
                           | otherwise = [x] ++ eliminarRepetidos (quitarTodos x (y:xs))  


quitarTodos :: ([Char],Int) -> [([Char],Int)] -> [([Char],Int)]
quitarTodos c [x] | fst c ==fst x =[]   
                  | otherwise =[x] 
quitarTodos c (x:xs) | fst c==fst x = quitarTodos c (xs)  
                     | otherwise = [x] ++ quitarTodos c (xs)





--EJERCICIO 2:
stockDeProducto :: [([Char],Int)] -> [Char] -> Int
stockDeProducto (x:xs) v | not (perteneceProducto v (x:xs)) =0
                         | perteneceProducto v (x:xs) = devuelveCantidad v (x:xs)

perteneceProducto :: [Char] -> [([Char],Int)] -> Bool
perteneceProducto v [] = False
perteneceProducto v [x] | v == fst x =True
                        | otherwise =False
perteneceProducto v (x:xs) | v==fst x =True
                           | otherwise = perteneceProducto v (xs)

devuelveCantidad :: [Char] -> [([Char],Int)] -> Int
devuelveCantidad v [x] | v==fst x =snd x
                       | otherwise =0
devuelveCantidad v (x:xs) | v==fst x =snd x
                          | otherwise = devuelveCantidad v (xs)





--EJERCICIO 3:
dineroEnStock :: [([Char],Int)] -> [([Char],Float)] -> Float
dineroEnStock (x:xs) (y:ys) = multiplicacion (suma2doElementoI (x:xs)) (suma2doElementoF (devuelvePreciosStock (x:xs) (y:ys)))

multiplicacion :: Int -> Float -> Float
multiplicacion n m = (fromIntegral n)*(m) 

suma2doElementoI :: [([Char],Int)] -> Int
suma2doElementoI [x] = snd x
suma2doElementoI (x:xs) = snd x + suma2doElementoI (xs)

suma2doElementoF :: [([Char],Float)] -> Float
suma2doElementoF [x] = snd x
suma2doElementoF (x:xs) = snd x + suma2doElementoF (xs)

devuelvePreciosStock :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)] 
devuelvePreciosStock [x] [y] | fst y ==fst x =[y]
                             | otherwise =[]
devuelvePreciosStock (x:xs) [y] | fst y ==fst x =[y]
                                | otherwise = devuelvePreciosStock (xs) [y]
devuelvePreciosStock (x:xs) (y:ys) | fst y ==fst x =[y] ++ devuelvePreciosStock (x:xs) (ys)
                                   | otherwise = devuelvePreciosStock (xs) [y] ++ devuelvePreciosStock (x:xs) (ys)





--EJERCICIO 4:
aplicarOferta :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)]
aplicarOferta (x:xs) [y] | stockDeProducto (x:xs) (fst y) > 10 = [(fst y, multiplicacion4 (snd y) (0.80))]
                         | stockDeProducto (x:xs) (fst y) <= 10 = [y]
aplicarOferta (x:xs) (y:ys) | stockDeProducto (x:xs) (fst y) > 10 = [(fst y, multiplicacion4 (snd y) (0.80))] ++ aplicarOferta (x:xs) (ys)
                            | stockDeProducto (x:xs) (fst y) <= 10 = [y] ++ aplicarOferta (x:xs) (ys)                      

multiplicacion4 :: Float -> Float -> Float
multiplicacion4 n m = n*m

