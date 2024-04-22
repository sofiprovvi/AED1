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

---2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] =False
pertenece n (x:xs)| n==x =True
                  | otherwise = pertenece n xs

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

--3)

--3.3
maximo :: [Integer] -> Integer
maximo (x:[]) =x
maximo (x:y:xs)|x>y = maximo (x:xs)
               |otherwise = maximo (y:xs)

--3.9
ordenar :: [Integer] -> [Integer]    
ordenar [] = []
ordenar (x:xs) = ordenar (quitar (maximo xs) xs) ++ [(maximo xs)] 
                 
