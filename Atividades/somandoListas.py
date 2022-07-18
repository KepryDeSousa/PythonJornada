
compras1 = (
    ('mouse',35),
    ('videogame','2500.40'),
    ('tela',80)
)
compras2 = (
    ('mouse',35),
    ('videogame','2500.05'),
    ('tela',80)
)

total = sum([float(y) for x,y in compras1])
total2 = sum([float(y) for x,y in compras2])
total = total+total2
print(f'{total}')

