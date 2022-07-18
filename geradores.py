"""
Interavel = conjunto que possue a capacidade de ser interativo
            listas, Strings...
Interador = valor que ganha a atribuição momentanea para fazer uso do interavel
            passando um valor de cada vez

gerador  = Uma função que retorna um iterador gerador.
           É parecida com uma função 'normal', 
           exceto pelo fato de conter expressões yield para produzir uma série de valores que podem ser usados em 
           um laço for ou que podem ser obtidos um de cada vez com a função next(). 
           Normalmente refere-se a uma função geradora, mas pode referir-se a um iterador gerador em alguns contextos. 
           Em alguns casos onde o significado desejado não está claro, 
           usar o termo completo evita ambiguidade.
           o mesmo reproduz por partes de cada vez do codigo para evitar desaceleração
           e como ele não lhe entrega todos os valores ao mesmo tempo seu consumo de memoria é menor
"""
import sys
import time

from numpy import matrix
matriz = list()
def gera():
    for n in range(1000000):
        matriz.append(n)
        
    return matriz

g = gera()
print(sys.getsizeof(g))

"updates"
"""

"""