from map import produtos

nova_lista = filter(lambda x: x['preco'] > 100,produtos)
for i in nova_lista:
    print(i)

"retornando apenas os parametros que dêem true com o argumento logico"