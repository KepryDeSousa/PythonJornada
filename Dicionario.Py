
"""
dicionario vs listas

No dicionario existe chave -> valor
nas listas são enumerados

"""

"Criando Dics"
d1 = {'chave': 'key1'}
#print(type(d1))
"método 2"
d1['nova_chave'] = 'ValordaChave2'
#print(type(d1))

"executando chave"
print(d1['nova_chave'])

"quando um dic tem a mesma chave repetida, o ultimo valor dela será o seu dado real"
d1 = {'chave': 'key1','chave': 'key1','chave': 'key2'}
#print(d1['chave'])

"comandos"
d1 = {'chave': 'key1'}

d1.update({'chave':'key4','str':'String'})
"update serve para atualizar um dic, contudo, ele pode adicionar e atualizar mais que um ao mesmo tempo"
"del d1['str'] "
"del funciona de forma literal"
print('str' in d1)
print('str' in d1.keys())
print('key4' in d1.values())
"keys() se existe aquele valor como chave"
"values() o mesmo, porém, com o valor da chave"
"items() para ver chave e valor "

"outros exemplos"

dados = {
    'cliente1': {
        'nome':'jorge',
        'idade': 18
    },
    'cliente2': {
        'nome':'José',
        'idade': 20
    }
}
for v,k in dados.items():
    print(f"Cliente : {v}, {k}")
    for j, k in k.items():
        print(f"{j} : {k}")

"interessante que se tiver uma lista dentro da tupla, a lista pode ser alterada"
"curiosidade: se usar o '=' para copiar você so estará copiano e sim pegando a localização"
".copy() ou deepcopy() para realizar copias razas"