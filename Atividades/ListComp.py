"loja"

tabela = (
    ('mouse',35.6),
    ('tela',18000.02),
    ('cpu','530')
)
total = sum([float(y) for x,y in tabela])
print(total)