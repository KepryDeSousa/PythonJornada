"""
Count / Intertools
"""
from itertools import count
contador = count(start=10,step=0.1); "por se tratar de um interador sem fim, cuidado com loops"
for i in contador:
    print(round(i,3))
    if i >= 100:
        break