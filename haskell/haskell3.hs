doubleMe::Int -> Int
doubleMe x = x + x

--PRACTICA 3: INTRODUCCION A HASKELL

--1) 

f::Int -> Int
f n | n==1 =8
    | n==4 =131
    | n==16 =16

g::Int -> Int
g n | n==8 =16
    | n==16 =4
    | n==131 =1

h :: Int -> Int
h n = f (g n)

--2)

--c)
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x>=y && x>=z =x
              | y>=x && y>=z =y
              | otherwise = z
--g)
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x/=z && x/=y && y/=z =x+y+z
                    | x==z && x==y && y==z =0
                    | z==x =y 
                    | z==y =x
                    | x==y =z

--i)
digitoUnidades:: Int -> Int
digitoUnidades x = mod x 10

--j)
digitoDecenas :: Int -> Int
digitoDecenas x = div (mod x 100) 10 

--a)
absoluto :: Int -> Int
absoluto x | x>=0 =x
           | x<0 =(-x)

--b)
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y | absoluto x > absoluto y =x
                   | otherwise =y

--d)
--GUARDAS
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y | x==0 || y==0 =True
              | otherwise =False

--PATTERN MATCHING
algunoEs0b :: Float -> Float -> Bool
algunoEs0b x 0 =True
algunoEs0b x _ =False

--e)
--GUARDAS
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x==0 && y==0 =True
              | otherwise =False

--PATTERN MATCHING
ambosSon0b :: Float -> Float -> Bool
ambosSon0b 0 0 =True
ambosSon0b _ _ =False

--f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x<=3 && y <=3 =True
                   | x>3 && x<=7 && y>3 && y<=7 =True
                   | x>7 && y>7 =True
                   | otherwise =False

--h)
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | x>0 && y>0 && mod x y ==0 =True
                 | otherwise =False

--3)

ambosNoSon0 :: Int -> Int -> Bool
ambosNoSon0 0 0 =False
ambosNoSon0 0 _ =False
ambosNoSon0 _ 0 =False
ambosNoSon0 _ _ =True
                   
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b | ambosNoSon0 a b && mod (-a) b==0 =True
                      | otherwise =False

--4)

--a)
prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt v w = fst v * fst w + snd v * snd w

--b)
digitoMenor :: (Float,Float) -> (Float,Float) -> Bool
digitoMenor v w | fst v < fst w && snd v < snd w =True
                | otherwise =False

--c)
distanciaPuntos :: (Float, Float) -> Float
distanciaPuntos v = absolutoV v

absolutoV :: (Float, Float) -> Float
absolutoV v | (snd v - fst v)>=0 =(snd v - fst v)
            | (snd v - fst v)<0 =(-(snd v - fst v))

--d)
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna v = fstV v + sndV v + trdV v        

fstV :: (x, y, z) -> x
fstV (x, y, z) = x

sndV :: (x, y, z) -> y
sndV (x, y, z) = y

trdV :: (x, y, z) -> z
trdV (x, y, z) = z

--e)
sumaSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumaSoloMultiplos v x | esMultiploDee (fstV v) x && esMultiploDee (sndV v) x && esMultiploDe (trdV v) x =fstV v + sndV v + trdV v
                      | esMultiploDee (fstV v) x && esMultiploDee (sndV v) x =fstV v + sndV v 
                      | esMultiploDee (fstV v) x && esMultiploDee (trdV v) x =fstV v + trdV v 
                      | esMultiploDee (sndV v) x && esMultiploDee (trdV v) x =sndV v + trdV v
                      | esMultiploDee (fstV v) x =fstV v
                      | esMultiploDee (sndV v) x =sndV v
                      | esMultiploDee (trdV v) x =trdV v
                      | otherwise =0
                      
esMultiploDee :: Int -> Int -> Bool
esMultiploDee x y | mod x y ==0 =True
                  | otherwise =False               

--f) 
posPrimerPar :: (Int, Int, Int) -> Int  
posPrimerPar v | esPar (fstV v) =1
               | esPar (fstV v) && esPar (sndV v) =1
               | esPar (fstV v) && esPar (trdV v) =1
               | esPar (fstV v) && esPar (sndV v) && esPar (trdV v) =1
               | esPar (sndV v) =2
               | esPar (sndV v) && esPar (trdV v) =2
               | esPar (trdV v) =3
               | otherwise =4

esPar :: Int -> Bool
esPar x | mod x 2==0 =True
        | otherwise =False 

--g)
crearPar :: a -> b -> (a,b) 
crearPar a b = (a, b) 

--h)
invertir :: (a, b) -> (b, a) 
invertir (a,b) = (b,a) 

--5)
todosMenores :: (Int, Int, Int) -> Bool
todosMenores v | (problemaF (fstV v) > problemaG (fstV v)) && (problemaF (sndV v) > problemaG (sndV v)) && (problemaF (trdV v) > problemaG (trdV v)) =True
               | otherwise =False

problemaF :: Int -> Int
problemaF n | n<=7 =n^2 
            | n>7 =2*n-1

problemaG :: Int -> Int
problemaG n | esPar n =div n 2 
            | otherwise =3*n+1

--6)
noesMultiplo4 :: Int -> Bool
noesMultiplo4 x | esMultiploDe x 4 =False
                | otherwise =True

noesMultiplo400 :: Int -> Bool
noesMultiplo400 x | esMultiploDe x 400 =False
                  | otherwise =True               

esMultiplo100 :: Int -> Bool
esMultiplo100 x | esMultiploDe x 100 && noesMultiplo400 x =True
                | otherwise =False

bisiesto :: Int -> Bool
bisiesto x | noesMultiplo4 x || esMultiplo100 x =False 
           | otherwise =True

--7)
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan v w = absolutoF (fstV v - fstV w) + absolutoF (sndV v - sndV w) + absolutoF (trdV v - trdV w)

absolutoF :: Float -> Float
absolutoF x | x>=0 =x
            | x<0 =(-x)

--8)
comparar :: Int -> Int -> Int  
comparar a b | (digitoDecenas a + digitoUnidades a) < (digitoDecenas b + digitoUnidades b) =1
             | (digitoDecenas a + digitoUnidades a) > (digitoDecenas b + digitoUnidades b) =(-1)
             | (digitoDecenas a + digitoUnidades a) == (digitoDecenas b + digitoUnidades b) =0

