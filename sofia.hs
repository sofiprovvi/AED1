--1)

--problema relacionesValidas (relaciones: seq⟨String x String⟩) : Bool {
 -- requiere: {True}
 -- asegura: {(res = true) <=> relaciones no contiene ni tuplas repetidas1, ni tuplas con ambas componentes iguales}
--}
--1 A los fines de este problema consideraremos que dos tuplas son iguales si el par de elementos que las componen (sin importar el orden) son iguales. 


iguales :: (String, String) -> (String, String) -> Bool
iguales v w |(fst v == snd w) && (fst w ==snd v) =False
            |(fst v == fst w) && (snd w ==snd v) =False
            |otherwise =True

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] =False
relacionesValidas (x:xs) | iguales (headseq x) (headseq (xs)) =False
                         | relacionesValidas (tail (xs)) =False
                         | otherwise =True
 

headseq :: [(String, String)] -> [(String, String)]
headseq (x:xs) = [x]

--2)

--problema personas (relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
-- requiere: {relacionesValidas(relaciones)}
-- asegura: {res no tiene elementos repetidos}
-- asegura: {res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
--}

--personas :: [(String, String)] -> [String]
--personas (x:xs) | 

noRepetidos :: [String] -> Bool
noRepetidos (x:[]) =True
noRepetidos (x:xs) | x == head xs =False
                   | otherwise = noRepetidos (tail xs)                      
 

