import pytest
from modelo2doparcial1 import verificar_transacciones , valor_minimo , valores_extremos , es_sudoku_valido

def test_verificar_transacciones():
    assert verificar_transacciones("ssrvvrrvvsvvsxrvvv") == 714
    assert verificar_transacciones("ssrvvvvsvvsvvv") == 14
    assert verificar_transacciones("s") == 0

def test_valor_minimo():
    assert valor_minimo([(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]) == -3.1
    assert valor_minimo([(12, 9.1),(20, 40.5),(12,52),(30,84)]) == 12
    assert valor_minimo([(1,0), (20, 50), (31,30)]) == 1
    assert valor_minimo([(1,0)]) == 1

valores_diarios = {'YPF':[(1,10),(15, 3), (31,100)],
                   'ALUA': [(1,0), (20, 50), (31,30)],
                   'GGAL': [(12, 9.1),(20, 40.5),(12,52),(30,84)],
                   'SOFIA':[(3, 560),(10,1500)]}

valores_diarios2 = {'YPF':[(3,100)],
                   'ALUA': [(0,50)],
                   'GGAL': [(9.1,84)],
                   'SOFIA':[(560, 1500)]}

def test_valores_extremos():
    assert valores_extremos(valores_diarios) == valores_diarios2    

m1 =  [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
      [9, 8, 7, 6, 4, 5, 3, 2, 1], 
      [0, 0, 0, 0, 0, 0, 1, 0, 0], 
      [0, 0, 0, 0, 0, 4, 0, 0, 0], 
      [0, 0, 0, 0, 6, 0, 0, 0, 0], 
      [0, 0, 0, 5, 0, 0, 0, 0, 0], 
      [0, 0, 4, 0, 0, 0, 0, 0, 0], 
      [0, 3, 0, 0, 0, 0, 0, 0, 0], 
      [2, 0, 0, 0, 0, 0, 0, 0, 0]]

m2 =  [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
      [9, 8, 7, 6, 4, 5, 5, 2, 1], 
      [0, 0, 0, 0, 0, 0, 1, 0, 0], 
      [0, 0, 0, 0, 0, 4, 0, 0, 0], 
      [0, 0, 0, 0, 6, 6, 0, 0, 0], 
      [0, 0, 0, 5, 0, 0, 0, 0, 0], 
      [0, 0, 4, 0, 0, 0, 0, 0, 0], 
      [0, 3, 0, 0, 0, 0, 0, 0, 0], 
      [2, 0, 0, 0, 0, 0, 0, 0, 0]]


matriz_ceros = [[0]*9]*9
matriz_fila_1_distinta = [list(range(1,10))] + [[0]*9]*8 

def test_es_sudoku_valido():
    assert es_sudoku_valido(m1) == True
    assert es_sudoku_valido(m2) == False
    assert es_sudoku_valido(matriz_ceros) == True 
    assert es_sudoku_valido(matriz_fila_1_distinta) == True   
