--MODELO 1ER PARCIAL 3:

--EJERCICIO 1:
cantMinuscula :: String -> Int
cantMinuscula s = longitud (listaCharMinuscula (stringChar (stringLista s)))

listaCharMinuscula :: [Char] -> [Char]
listaCharMinuscula [] = []
listaCharMinuscula [x]  | charMinuscula x =[x]
                        | otherwise =[]
listaCharMinuscula (x:xs) | charMinuscula x =[x] ++ listaCharMinuscula (xs) 
                          | otherwise =listaCharMinuscula (xs)              

charMinuscula :: Char -> Bool
charMinuscula a  | pertenece a abc =True
                 | otherwise =False
            where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

pertenece :: (Eq t) => t ->[t]-> Bool  
pertenece s [] =False
pertenece s [x] | s==x =True
                | otherwise =False
pertenece s (x:xs) | s==x =True
                   | otherwise = pertenece s (xs)                            
                 
stringLista :: String -> [String]
stringLista s = [s]

stringChar :: [String] -> [Char]
stringChar (x:xs) | x== " " =[]
                  | otherwise = x ++ stringChar (xs)
stringChar (xs) =[]                  

longitud :: (Eq t) => [t] -> Int
longitud [] =0
longitud [x] =1
longitud (x:xs) = 1 + longitud (xs)   



--EJERCICIO 2:
maximoCambios :: [String] -> String
maximoCambios (x:[]) | cantChar (x:[]) == cantMinusculaListaString (x:[]) =x
                     | otherwise = ""
maximoCambios (x:xs) | cantChar [x] == cantMinusculaListaString [x] =x
                     | otherwise = maximoCambios (xs)                    

cantMinusculaListaString :: [String] -> Int
cantMinusculaListaString [x] = cantMinuscula x
cantMinusculaListaString (x:xs) = cantMinuscula x + cantMinusculaListaString (xs)   

cantChar :: [String] -> Int
cantChar (x:xs) = longitud (stringChar (x:xs))



--EJERCICIO 3:
desplazar :: Char -> Int -> Char
desplazar c n | pertenece3 c && n>=0 =desplazarPositivo c n
              | pertenece3 c && n<=(-1) =desplazarNegativo c n
              | nopertenece3 c =c

desplazarPositivo :: Char -> Int -> Char 
desplazarPositivo c n | n>=0 && pertenece3 c && ((posicionC c + n) <= 25) =elementoPosicion (posicionC c + n) 
                      | otherwise = elementoPosicionR (posicionC c +1)
                      
desplazarNegativo :: Char -> Int -> Char
desplazarNegativo c n | n<=(-1) && ((posicionC c + n) >= 0) = elementoPosicion (posicionC c + n)
                      | otherwise =elementoPosicionR (posicionC c)

pertenece3 :: Char -> Bool  
pertenece3 s | pertenece s abc =True
             | otherwise =False
     where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

nopertenece3 :: Char -> Bool  
nopertenece3 s | pertenece s abc =False
               | otherwise =True
     where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']      
    
posicionC :: Char -> Int
posicionC c = elementosLista c abc
    where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 


elementosLista :: Char -> [Char] -> Int
elementosLista c (x:y:xs) | c==x =0
                          | otherwise = 1 + elementosLista c (y:xs)  
elementosLista c (xs) =0                                           

elementoPosicion :: Int -> Char                             
elementoPosicion n = elementoPosicionAux n abc
   where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

reverso :: [Char] -> [Char]
reverso [x] = [x]
reverso (x:y:[]) = [y] ++ [x]
reverso (x:xs) = reverso (xs) ++ [x]

elementoPosicionR :: Int -> Char 
elementoPosicionR n = elementoPosicionAux n (reverso (abc))
   where abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

elementoPosicionAux :: Int -> [Char] -> Char
elementoPosicionAux n (x:y:xs) | n==0 =x
                               | n==1 =y
                               | n>1 = elementoPosicionAux (n-2) (xs)



--EJERCICIO 4:
codificar :: String -> Int -> String
codificar s n = charString (desplazar4 (listaCharMinuscula (stringChar (stringLista s))) n)

desplazar4 :: [Char] -> Int -> [Char]
desplazar4 (x:[]) n = [desplazar x n]
desplazar4 (x:xs) n = [desplazar x n] ++ desplazar4 (xs) n

charString :: [Char] -> String
charString (x:xs) | x== ' ' =""
                  | otherwise = [x] ++ charString (xs)
charString (xs) =[]   



--EJERCICIO 5:
decodificar :: String -> Int -> String
decodificar s n = charString (desplazar55 (listaCharMinuscula (stringChar (stringLista s))) n)

desplazar55 :: [Char] -> Int -> [Char]
desplazar55 (x:[]) n = [desplazar x (-n)]
desplazar55 (x:xs) n = [desplazar x (-n)] ++ desplazar55 (xs) n






