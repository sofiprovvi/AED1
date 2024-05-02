--GUIA 5: RECURSION SOBRE LISTAS

--1)

---1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--1.2
ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo xs

--1.3
principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x : principio xs

--1.4
reverso :: [t] -> [t]
reverso (x:[]) = [x]
reverso (x:xs) = reverso xs ++ reverso [x]


--2)

--2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] =False
pertenece n (x:xs)| n==x =True
                  | otherwise = pertenece n xs

--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) =True
todosIguales (x:xs) | pertenece x xs =todosIguales (xs)
                    | otherwise =False       

--2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:[]) =True
todosDistintos (x:xs) | pertenece x xs =False
                      | otherwise =todosDistintos xs 
                       

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos [] =False
hayRepetidos (x:xs) | pertenece x xs =True
                    | otherwise = hayRepetidos xs  

--2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] =[]
quitar n (x:xs) | n==x =xs
                | otherwise = x: quitar n xs   

--2.6
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos n (x:[]) =[]    
quitarTodos n (x:xs) | n==x = quitarTodos n xs 
                     | n/=x = x: quitarTodos n xs 

--2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos (x:[]) =[x]   
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs
                         | otherwise = x: eliminarRepetidos xs                                            

--2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) | listaPertenece (x:xs) (y:ys) && listaPertenece (y:ys) (x:xs) =True
                              | otherwise =False 

listaPertenece :: (Eq t) => [t] -> [t] -> Bool
listaPertenece (_) ([]) =False
listaPertenece ([]) (_) =True
listaPertenece (x:xs) (y:ys) | pertenece x (y:ys) =listaPertenece xs (y:ys)
                             | otherwise =False 

--2.9
capicua :: (Eq t) => [t] -> Bool
capicua (x:xs) | (x:xs) == reverso (x:xs) =True
               | otherwise =False



--3)

--3.1
sumatoria :: [Integer] -> Integer
sumatoria (x:[]) = x
sumatoria (x:xs) = x + sumatoria (xs)

--3.2
productoria :: [Integer] -> Integer
productoria (x:[]) = x
productoria (x:xs) = x * productoria (xs)

--3.3
maximo :: [Integer] -> Integer
maximo (x:[]) =x
maximo (x:y:xs)|x>y = maximo (x:xs)
               |otherwise = maximo (y:xs)

--3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n (x:[]) = [(x+n)] 
sumarN n (x:xs) = (x+n) : sumarN n (xs)  

--3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

--3.7
pares :: [Integer] -> [Integer]
pares (x:[]) | esPar x = [x]
pares (x:xs) | (esPar x) = x: pares (xs)
             | otherwise = pares(xs)

esPar :: Integer -> Bool
esPar x | mod x 2 ==0 =True 
        | otherwise =False 

--3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n (x:[]) | esMultiploN x n = [x]
multiplosDeN n (x:xs) | esMultiploN x n = x: multiplosDeN n (xs)
                      | otherwise = multiplosDeN n (xs)

esMultiploN :: Integer -> Integer -> Bool
esMultiploN x n | (mod x n) ==0 =True
                | otherwise =False

--3.9
ordenar :: [Integer] -> [Integer]    
ordenar [] = []
ordenar (x:xs) = ordenar (quitar (maximo xs) xs) ++ [(maximo xs)] 


--4)

--a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos (x:y:[]) | (x== ' ') && x==y = [y] 
sacarBlancosRepetidos (x:y:xs) | (x== ' ') && x==y = sacarBlancosRepetidos ([y] ++ (xs))
                               | otherwise = [x] ++ sacarBlancosRepetidos ([y] ++ (xs))  
sacarBlancosRepetidos (xs) = xs                                   

--b)
contarPalabras :: [Char] -> Integer 
contarPalabras (x:xs) = cantidadBlancos (sacarExtremosYRepetidos (x:xs)) + 1

cantidadBlancos :: [Char] -> Integer
cantidadBlancos (x:[]) | (x== ' ') =1
cantidadBlancos (x:xs) | (x== ' ') = 1 + cantidadBlancos (xs)
                       | (x/= ' ') = cantidadBlancos (xs) 
cantidadBlancos (xs) = 0                      

sacarBlancoPrincipioo :: [Char] -> [Char]  
sacarBlancoPrincipioo (x:xs) | principioo (x:xs) == ' ' =xs
                             | otherwise = (x:xs) 

sacarBlancoUltimo :: [Char] -> [Char]
sacarBlancoUltimo (x:[]) | ultimo (x:[])== ' ' =[]
                         | otherwise =(x:[])
sacarBlancoUltimo (x:xs) | ultimo (x:xs) == ' ' = x: sacarBlancoUltimo (xs)
                         | otherwise =(x:xs)
                         
sacarExtremos :: [Char] -> [Char]
sacarExtremos (x:xs) = sacarBlancoUltimo (sacarBlancoPrincipioo (x:xs))

sacarExtremosYRepetidos :: [Char] -> [Char]
sacarExtremosYRepetidos (x:xs) = sacarExtremos (sacarBlancosRepetidos (x:xs))

principioo :: [t] -> t
principioo (x:[]) = x
principioo (x:xs) = x


--c)                               
primeraPalabra ::  [Char] -> [Char]
primeraPalabra ([]) = ([])
primeraPalabra (x:xs) | x== ' ' =[]
                      | otherwise = x: primeraPalabra (xs)

quitarPrimeraPalabra :: [Char] -> [Char] 
quitarPrimeraPalabra ([]) = ([])
quitarPrimeraPalabra (x:y:xs) | [x]++[y] == primeraPalabra ((x:y:xs)) =sacarExtremosYRepetidos (xs)  
                              | [x] == primeraPalabra ((x:y:xs)) = sacarExtremosYRepetidos (y:xs)
                              | [x]++[y] /= primeraPalabra ((x:y:xs)) = sacarExtremosYRepetidos (quitarPrimeraPalabra (xs)) 

palabras :: [Char] -> [[Char]] 
palabras (x:y:xs) | contarPalabras (x:y:xs)==1 = [sacarExtremosYRepetidos (x:y:xs)]
                  | contarPalabras (x:y:xs)>1 = [primeraPalabra (((x:y:xs)))] ++ palabras (quitarPrimeraPalabra ((x:y:xs)))
                  | contarPalabras (x:y:xs)==0 =[]


--d)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:xs) | contarPalabras (x:xs) ==1 = sacarExtremosYRepetidos (x:xs)
                       | contarPalabras (x:xs) ==0 =[]
                       | (contarPalabras (x:xs) ==2) && cantidadChar1 (x:xs) < cantidadChar2 (x:xs) =segundaPalabra (x:xs)
                       | (contarPalabras (x:xs) ==2) && cantidadChar1 (x:xs) > cantidadChar2 (x:xs) =primeraPalabra (sacarExtremosYRepetidos (x:xs))
                       | (contarPalabras (x:xs) >2) && cantidadChar1 (x:xs) < cantidadChar2 (x:xs) =palabraMasLarga (quitarPrimeraPalabra (x:xs))
                       | (contarPalabras (x:xs) >2) && cantidadChar1 (x:xs) > cantidadChar2 (x:xs) =palabraMasLarga (quitarSoloSegundaPalabra (x:xs))

cantidadChar :: [Char] -> Integer
cantidadChar (x:y:xs) | contarPalabras (x:y:xs)==1 =longitud (sacarExtremosYRepetidos (x:y:xs))
                      | otherwise =0                    

cantidadChar1 :: [Char] -> Integer
cantidadChar1 (x:y:xs) = cantidadChar (primeraPalabra (x:y:xs))

cantidadChar2 :: [Char] -> Integer
cantidadChar2 (x:y:xs) = cantidadChar (segundaPalabra (x:y:xs))

segundaPalabra :: [Char] -> [Char]
segundaPalabra (x:xs) = sacarExtremosYRepetidos (primeraPalabra (quitarPrimeraPalabra (x:xs)))

quitarSoloSegundaPalabra :: [Char] -> [Char]
quitarSoloSegundaPalabra (x:xs) = (primeraPalabra (x:xs)) ++ [' '] ++ (quitarPrimeraPalabra (quitarPrimeraPalabra (x:xs)))
