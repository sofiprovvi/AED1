--EJERCICIO 1:
nuevaMatriz :: [Int] -> [[Int]] -> [[Int]]
nuevaMatriz (x:xs) [y] = [sumaElementos (x:xs) y]
nuevaMatriz (x:xs) (y:ys) = [sumaElementos (x:xs) y] ++ nuevaMatriz (x:xs) (ys)
nuevaMatriz (x:xs) [] = []

sumaElementos :: [Int] -> [Int] -> [Int]
sumaElementos [x] [y] = [(x+y)]
sumaElementos (x:xs) (y:ys) = [(x+y)] ++ sumaElementos (xs) (ys)

--m = [[1,4,3,2],
--     [6,1,8,9],
--     [2,9,7,4],
--     [3,2,3,3]
--     ]

--s = [3,2,8,4]





--EJERCICIO 2:
esDamero :: [[Int]] -> Bool
esDamero (x:xs) | filasValidas (x:xs) && columnasValidas (x:xs) && (longitud (x:xs)==8) =True
                | otherwise =False

longitud :: [[Int]] -> Int
longitud [x] = 1
longitud (x:xs) = 1 + longitud (xs)  

secuenciaValida :: [Int] -> Bool
secuenciaValida (x:y:[]) | x==1 && y==0 =True
                         | x==0 && y==1 =True
                         | otherwise =False
secuenciaValida (x:y:xs) | x==1 && y==0 =secuenciaValida (y:xs)
                         | x==0 && y==1 =secuenciaValida (y:xs)
                         | otherwise =False

filasValidas ::[[Int]] -> Bool
filasValidas [x] | secuenciaValida x =True
                 | otherwise =False
filasValidas (x:xs) | secuenciaValida x =filasValidas (xs)
                    | otherwise =False

quitarPrimerElemento :: [Int] -> [Int]
quitarPrimerElemento (x:xs) = xs
quitarPrimerElemento [] = []

quitarPrimeraColumna :: [[Int]] -> [[Int]]
quitarPrimeraColumna [x] = [quitarPrimerElemento x]
quitarPrimeraColumna (x:xs) = [quitarPrimerElemento x] ++ quitarPrimeraColumna (xs)
quitarPrimeraColumna [] = []                    

primeraColumna :: [[Int]] -> [Int]
primeraColumna [] = []
primeraColumna [x] = [head x]
primeraColumna (x:xs) = [head x] ++ primeraColumna (xs)

columnas :: [[Int]] -> [[Int]]
columnas [] = []
columnas ([]:_) = []
columnas (x:xs) = [primeraColumna (x:xs)] ++ columnas (quitarPrimeraColumna(x:xs))

columnasValidas :: [[Int]] -> Bool
columnasValidas (x:xs) | filasValidas (columnas (x:xs)) =True
                       | otherwise =False


--tablero = [[1,0,1,0,1,0,1,0],
--     [0,1,0,1,0,1,0,1],
--     [1,0,1,0,1,0,1,0],
--     [0,1,0,1,0,1,0,1],
--     [1,0,1,0,1,0,1,0],
--     [0,1,0,1,0,1,0,1],
--     [1,0,1,0,1,0,1,0],
--     [0,1,0,1,0,1,0,1]
--]

--falso_tablero = [[0,1,0],
--                 [1,0,1],
--                 [0,1,0]
--                 ]