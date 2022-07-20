"""
Itertools

"""
from itertools import combinations as comb;

lista = ['joao','maria','jose','renata','alencar','juan','melissa','jorge']

for lista1 in comb(lista,3):
    print(lista1)
"combinations nos tras a combinação entre a listas, caso a ordem não seja nescessaria "

from itertools import permutations as per;
for lista1 in per(lista,3):
    print(lista1)
"agora em ordem"
"Ambos respeitam a ordem e repetem os valores unicos"