module SolucionT2 where

--EJERCICIO 1:
generarStock :: [[Char]] -> [([Char],Int)]
generarStock [] = []
generarStock [x] = [(x , cantidadDeApariciones x [x])] 
generarStock (x:xs) = eliminarRepetidos ([(x, cantidadDeApariciones x (x:xs))] ++ generarStock (xs))

cantidadDeApariciones :: [Char] -> [[Char]] -> Int
cantidadDeApariciones c [x] | c==x  =1
                            | otherwise =0
cantidadDeApariciones c (x:xs) | c==x =1 + cantidadDeApariciones c (xs)
                               | c/=x = cantidadDeApariciones c (xs)

eliminarRepetidos :: [([Char],Int)] -> [([Char],Int)]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:y:[]) | (fst x)== (fst y) =[x]
                           | otherwise =[x]++[y]
eliminarRepetidos (x:y:xs) | (fst x)==(fst y) = eliminarRepetidos (x:xs)   
                           | otherwise = [x] ++ eliminarRepetidos (quitarTodos x (y:xs))  


quitarTodos :: ([Char],Int) -> [([Char],Int)] -> [([Char],Int)]
quitarTodos c [x] | fst c ==fst x =[]   
                  | otherwise =[x] 
quitarTodos c (x:xs) | fst c==fst x = quitarTodos c (xs)  
                     | otherwise = [x] ++ quitarTodos c (xs)





--EJERCICIO 2:
stockDeProducto :: [([Char],Int)] -> [Char] -> Int
stockDeProducto [] v = 0
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
dineroEnStock [] [] = 0
dineroEnStock [] (p:precios) = 0
dineroEnStock (s:stock) (p:precios) = dineroPorProductosEnStock (s:stock) (devuelvePreciosEnStock (s:stock) (p:precios))

--devuelve la lista de precios de los productos que sí estan en stock:
devuelvePreciosEnStock :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)] 
devuelvePreciosEnStock [s] [p] | fst s ==fst p =[p]
                               | otherwise =[]
devuelvePreciosEnStock (s:stock) [p] | fst s ==fst p =[p]
                                     | otherwise = devuelvePreciosEnStock (stock) [p]
devuelvePreciosEnStock (s:stock) (p:precios) | fst s ==fst p =[p] ++ devuelvePreciosEnStock (s:stock) (precios)
                                             | otherwise = devuelvePreciosEnStock (stock) [p] ++ devuelvePreciosEnStock (s:stock) (precios)

multiplicacion :: Int -> Float -> Float
multiplicacion n m = (fromIntegral n)*(m) 

--multiplicación de la cantidad del producto en stock por su precio:
dineroPorProductoEnStock :: ([Char],Int) -> [([Char],Float)] -> Float
dineroPorProductoEnStock s (p:precios) | fst s == fst p =multiplicacion (snd s) (snd p)
                                       | otherwise = dineroPorProductoEnStock s (precios)

--suma de las multiplicaciones de cada producto:
dineroPorProductosEnStock :: [([Char],Int)] -> [([Char],Float)] -> Float
dineroPorProductosEnStock [s] (p:precios) = dineroPorProductoEnStock s (p:precios)
dineroPorProductosEnStock (s:stock) (p:precios) = dineroPorProductoEnStock s (p:precios) + dineroPorProductosEnStock (stock) (p:precios)




--EJERCICIO 4:
aplicarOferta :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)]
aplicarOferta [] (y:ys) = []
aplicarOferta (x:xs) [] = []
aplicarOferta (x:xs) [y] | stockDeProducto (x:xs) (fst y) > 10 = [(fst y, multiplicacion4 (snd y) (0.80))]
                         | stockDeProducto (x:xs) (fst y) <= 10 = [y]
aplicarOferta (x:xs) (y:ys) | stockDeProducto (x:xs) (fst y) > 10 = [(fst y, multiplicacion4 (snd y) (0.80))] ++ aplicarOferta (x:xs) (ys)
                            | stockDeProducto (x:xs) (fst y) <= 10 = [y] ++ aplicarOferta (x:xs) (ys)                      

multiplicacion4 :: Float -> Float -> Float
multiplicacion4 n m = n*m

