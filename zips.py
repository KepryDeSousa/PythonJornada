"""
interaveis com zip

"""
from itertools import zip_longest
cidade = ['Sao paulo','salvador','fortaleza','caucaia']
estados = ['SP','BH','CE']
cidades_estdos = zip_longest(cidade,estados,fillvalue = 'Estado')
for i in cidades_estdos:
    print(i)

"""
com o zip ele produz uma tupla mais se houve um valor a mais em um lado 
ele simplismente cortará

com zip_longest 
ele irar preencher com o valor padrao ou que vc atruibuir no default
ex :
cidades_estdos = zip_longest(cidade,estados,  fillvalue = 'Estado')
"""