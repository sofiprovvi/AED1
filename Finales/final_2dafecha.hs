nuevaSecuencia :: [Int] -> [Int] -> [Int]
nuevaSecuencia (x:[]) (y:ys) | x <= longitud (y:ys) =[maximo (subsecuencia x (y:ys))]
                             | otherwise = [ultimo (y:ys)]
nuevaSecuencia (x:xs) (y:ys) | x <= longitud (y:ys) =[maximo (subsecuencia x (y:ys))] ++ nuevaSecuencia (xs) (y:ys)
                             | otherwise = [ultimo (y:ys)] ++ nuevaSecuencia (xs) (y:ys)


ultimo :: [Int] -> Int
ultimo [x] = x
ultimo (x:xs) = ultimo (xs)

longitud :: [Int] -> Int
longitud [x] = 1
longitud (x:xs) = 1 + longitud (xs)

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:[]) | x>=y =x
                | x<y =y
maximo (x:y:xs) | x>=y =maximo (x:xs)
                | x<y =maximo (y:xs)

subsecuencia :: Int -> [Int] -> [Int]
subsecuencia n (y:ys) | n==0 =[y]
                      | n>0 = [y] ++ subsecuencia (n-1) (ys)                 