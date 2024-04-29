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
f13 n m = f13n n m + f13m n m 

f13n :: Integer -> Integer -> Integer
f13n n m | n==1 && m==m =1
         | n>1 && m==m =f13n (n-1) m + n^m

f13m :: Integer -> Integer -> Integer
f13m n m | n==n && m==1 =n         
         | m>1 && n==n =f13m n (m-1) + n^m


--14)
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = sumaPotenciasN q n m + sumaPotenciasM q n m

sumaPotenciasN :: Integer -> Integer -> Integer -> Integer
sumaPotenciasN q n m | n==1 && m==m && q==q =q^(1+m)
                     | n>1 && m==m && q==q =(sumaPotenciasN q (n-1) m) + q^(n+m)

sumaPotenciasM :: Integer -> Integer -> Integer -> Integer
sumaPotenciasM q n m | n==n && m==1 && q==q =q^(1+n)
                     | m>1 && n==n && q==q =(sumaPotenciasM q n (m-1)) + q^(n+m)                   


--15)

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales p q = sumaRacionalesP p q + sumaRacionalesQ p q 

sumaRacionalesP :: Integer -> Integer -> Float
sumaRacionalesP p q | p==1 && q==q = 1/(fromIntegral q)
                    | p>1 && q==q =sumaRacionalesP (p-1) q + (fromIntegral p) / (fromIntegral q)

sumaRacionalesQ :: Integer -> Integer -> Float
sumaRacionalesQ p q | p==p && q==1 =fromIntegral p
                    | p==p && q>1 = sumaRacionalesQ p (q-1) + (fromIntegral p) / (fromIntegral q)               


--16)

--a)
menorDivisor :: Integer -> Integer
menorDivisor n = divisorDe n 2
  
divisorDe :: Integer -> Integer -> Integer
divisorDe n i | mod n i ==0 =i
              | otherwise =divisorDe n (i+1)

--b)

esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n ==n =True
          | otherwise =False

--c)

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m | divisoresEnComun n m 2 ==True =False
                | otherwise =True   

divisoresEnComun :: Integer -> Integer -> Integer -> Bool
divisoresEnComun n m i | i > n || i > m =False
                       | divisorDe n i == divisorDe m i =True   
                       | otherwise = divisoresEnComun n m (i+1)

--d)
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo i = encontrarPrimo i 2

encontrarPrimo :: Integer -> Integer -> Integer
encontrarPrimo i n | esPrimo n && i == 1 = n
                   | esPrimo n = encontrarPrimo (i-1) (n+1)
                   | otherwise = encontrarPrimo i (n+1)


--17)

esFibonacci :: Integer -> Bool
esFibonacci n | perteneceFibonacci n 1 =True 
              | otherwise =False

perteneceFibonacci :: Integer -> Integer -> Bool
perteneceFibonacci n i | n < fibonacci i =False
                       | n == fibonacci i =True
                       | otherwise = perteneceFibonacci n (i+1)


--18)

--problema mayorDigitoPar (n: N) : N {
--requiere: { True }
--asegura: { resultado es el mayor de los dıgitos pares de n. Si n no tiene ning´un dıgito par, entonces resultado es -1.}
--}

--mayorDigitoPar :: Integer -> Integer
--mayorDigitoPar n |
