--GUIA 4: RECURSION SOBRE NUMEROS ENTEROS

--1)

--GUARDAS:
fibonacci :: Integer -> Integer
fibonacci n | n==0 =0
            | n==1 =1
            | n>=1 = fibonacci (n-1) + fibonacci (n-2)

--PATTERN MATCHING:
fibonacci1 :: Integer -> Integer
fibonacci1 0 =0
fibonacci1 1 =1
fibonacci1 n =fibonacci (n-1) + fibonacci (n-2)           

--2)
parteEntera :: Float -> Integer
parteEntera x | x>=0 && x<1 =0
              | x>=1 =(1 + parteEntera (x-1)) 
              | x<0 && x>=(-1) =(-1)
              | x<=(-1) =(-1 + parteEntera (x+1)) 

--3)
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x==y || y==1 =True
                | x-y==0 =True
                | y>x =False
                | otherwise = esDivisible (x-y) y

--4)
sumaImpares :: Integer -> Integer  
sumaImpares n | n==1 =1
              | n>1 =(2*n-1) + sumaImpares (n-1)     

--5)
medioFact :: Integer -> Integer
medioFact n | n==0 =1
            | n==1 =1
            | n>1 = n * medioFact (n-2) 

--6)
sumaDigitos :: Integer -> Integer
sumaDigitos n | n<10 =n
              | n>=10 = sumaDigitos (div n 10) + sumaDigitos (mod n 10)

--7)
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n<10 =True
                      | n>=10 = (mod n 10 == mod(div n 10) 10) && todosDigitosIguales (div n 10)

--8)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i =mod n 10
                 | cantDigitos n > i =iesimoDigito (div n 10) i

cantDigitos :: Integer -> Integer
cantDigitos n | n<10 =1
              | n>10 =cantDigitos (div n 10) + cantDigitos (mod n 10)

--9) 
esCapicua :: Integer -> Bool
esCapicua n | n<10 =True
            | n>10 && (iesimoDigito n 1) /= (mod n 10) =False
            | otherwise = n>10 && esCapicua (mod(div n 10) 10)

--10)

--a)
f1 :: Integer -> Integer
f1 n | n==1 =2^1
     | n>1 =f1 (n-1) + 2^n

--b)
f2 :: Integer -> Float -> Float
f2 n q | n==1 && q==q =q
       | n>=1 && q==q  =((f2 (n-1) q) + q^n)

--c)
f3 :: Integer -> Float -> Float
f3 n q | n==1 && q==q =q + q^(2*n)
       | n>=1 && q==q  =((2*(f3 (n-1) q)) + 2 + (q^(2*n)))            

--d)
f4 :: Integer -> Float -> Float
f4 n q | n==1 && q==q =q + q^(2*n)
       | n>=1 && q==q  =(2*(f4 (n-1) q)) + q^(2*n)        


--11)

 --a)

factorial :: Integer -> Integer
factorial n | n==0 =1
            | otherwise = factorial (n-1)*n

eAprox :: Integer -> Float
eAprox n | n==0 = 1 / (fromIntegral (factorial n))
         | n>0 = 1/(fromIntegral (factorial n)) + eAprox (n-1)
 
--b)
e :: Float
e = eAprox 10 


--12)

f12 :: Integer -> Float
f12 n | n==1 =2
      | n>1 = 2 + 1/(f12 (n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (f12 n) -1

--13)

f13 :: Integer -> Integer -> Integer
f13 n m | n==1 && m==m =m
        | n>=1 && m==m =(f13 (n-1) (m-1)) + ((m-1)^n) + (f13 (n-1) m) + (m^n)