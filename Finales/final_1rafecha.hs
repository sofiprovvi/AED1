esSudokuValido :: [[Int]] -> Bool
esSudokuValido (x:xs) | filasNoValidas (x:xs) =False
                      | columnasNoValidas (x:xs) =False
                      | otherwise =True

hayRepetidos :: [Int] -> Bool
hayRepetidos (x:y:[]) | (x==y && (x/=0) && (y/=0)) =True
                       | otherwise =False
hayRepetidos (x:y:xs) | (x==y && (x/=0) && (y/=0)) =True
                       | otherwise = hayRepetidos (x:xs) || hayRepetidos (y:xs)

filasNoValidas :: [[Int]] -> Bool
filasNoValidas [x] | hayRepetidos x =True
                   | otherwise =False
filasNoValidas (x:xs) | hayRepetidos x =True
                      | otherwise = filasNoValidas (xs)                   

quitarPrimerElemento :: [Int] -> [Int] 
quitarPrimerElemento [] = []
quitarPrimerElemento (x:xs) = xs

quitarPrimeraColumna :: [[Int]] -> [[Int]]
quitarPrimeraColumna [x] = [quitarPrimerElemento x]
quitarPrimeraColumna (x:xs) = [quitarPrimerElemento x] ++ quitarPrimeraColumna (xs)

primeraColumna :: [[Int]] -> [Int]
primeraColumna [x] = [head x]
primeraColumna (x:xs) = [head x] ++ primeraColumna (xs)

columnas :: [[Int]] -> [[Int]]
columnas [] = []
columnas ([]:_) = []
columnas (x:xs) = [primeraColumna (x:xs)] ++ columnas (quitarPrimeraColumna (x:xs))

columnasNoValidas :: [[Int]] -> Bool
columnasNoValidas (x:xs) | filasNoValidas (columnas (x:xs)) =True
                         | otherwise =False


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

