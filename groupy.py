from ctypes.wintypes import PINT
from itertools import groupby


alunos = [
    {'nome': 'luiz', 'nota': 10},
    {'nome': 'leticia', 'nota': 8},
    {'nome': 'fab', 'nota': 9},
    {'nome': 'rose', 'nota': 6},
    {'nome': 'joao', 'nota': 5},
    {'nome': 'joana', 'nota': 7}
]
alunos.sort(key=lambda item: item['nota'])
aluno_agrupados = groupby(alunos,lambda i: i['nota'])
for i in aluno_agrupados:
    print(i)
