esSudokuValido :: [[Int]] -> Bool
esSudokuValido (x:xs) | filasNoValidas (x:xs) =False
                      | columnasNoValidas (x:xs) =False
                      | otherwise =True

hayRepetidosF :: [Int] -> Bool
hayRepetidosF (x:y:[]) | (x==y && (x/=0) && (y/=0)) =True
                       | otherwise =False
hayRepetidosF (x:y:xs) | (x==y && (x/=0) && (y/=0)) =True
                       | otherwise = hayRepetidosF (x:xs) || hayRepetidosF (y:xs)

filasNoValidas :: [[Int]] -> Bool
filasNoValidas [x] | hayRepetidosF x =True
                   | otherwise =False
filasNoValidas (x:xs) | hayRepetidosF x =True
                      | otherwise = filasNoValidas (xs)                   

principio :: [Int] -> Int
principio [] = 0
principio (x:xs) = x

quitarPrincipio :: [Int] -> [Int] 
quitarPrincipio [] = [0]
quitarPrincipio (x:xs) = xs

quitarPrincipioLista :: [[Int]] -> [[Int]]
quitarPrincipioLista [x] = [quitarPrincipio x]
quitarPrincipioLista (x:xs) = [quitarPrincipio x] ++ quitarPrincipioLista (xs)

hayRepetidosC :: [[Int]] -> Bool
hayRepetidosC (x:y:[]) | ((principio x == principio y)  && ((principio x)/=0) && ((principio y)/=0)) =True
                       | otherwise =False
hayRepetidosC (x:y:xs) | ((principio x == principio y)  && ((principio x)/=0) && ((principio y)/=0)) =True
                       | otherwise = hayRepetidosC (x:xs) || hayRepetidosC (y:xs)

columnasNoValidas :: [[Int]] -> Bool
columnasNoValidas (xs) = False
columnasNoValidas (x:y:xs) | hayRepetidosC (x:y:xs) =True
                           | otherwise =columnasNoValidas (quitarPrincipioLista (x:y:xs)) 


m :: [[Int]] -> [[Int]]
m (x:xs) = [[1,2,3,4,5,6,7,8,9],
           [9,8,7,6,4,5,3,2,1],
           [0,0,0,0,0,0,1,0,0],
           [0,0,0,0,0,4,0,0,0],
           [0,0,0,0,6,0,0,0,0],
           [0,0,0,5,0,0,0,0,0],
           [0,0,4,0,0,0,0,0,0],
           [0,3,0,0,0,0,0,0,0],
           [2,0,0,0,0,0,0,0,0]]

