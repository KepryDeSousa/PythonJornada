from map import pessoas, produtos

"pode passar uma função como primeiro parametro no map na sequencia a lista"


def AumentaPreco(p):
    p['preco' ] = p['preco'] *1.20
    return p
 

nova_list = map( AumentaPreco,produtos)

for i in nova_list:
    print(i)


for i in produtos:
    print(i) 