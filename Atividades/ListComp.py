"loja"

tabela = (
    ('mouse',35.6),
    ('tela',180.02),
    ('cpu','530')
)
total = sum([float(y) for x,y in tabela])
print(total)