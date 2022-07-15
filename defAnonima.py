"""
Ou expressões lambda

"""
lista = [
    ['p1',50],
    ['p2',51],
    ['p3',52],
    ['p4',53],
    ['p5',555],
]
lista.sort(key= lambda item: item[1], reverse=True)
print(lista)
print(sorted(lista, key= lambda i: i[1]))
"""sempre que precisar passar uma função ou um metodo dentro de outro
as funçoes lambda ou anonimas são otimas pedidas"""
