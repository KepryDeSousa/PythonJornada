"Funções"
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
from ast import arg


def saudacoes(nome):
    return f"Saudacoes {nome}"


nome = "Jorgin"
print(saudacoes(nome))

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""

def soma(*args):
   contador = 0
   lista = list(args)
   for i in lista :
        contador += i
   return contador

somar = soma(1,4,5,8,9,0,606,9339393)
print(somar)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def percentural(valor1, valor2):
    return (valor1 + (valor2 * 0.10))
 
print(percentural(10,47))

"""4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.



def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n
 
 
from random import randint
 
for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))

"""