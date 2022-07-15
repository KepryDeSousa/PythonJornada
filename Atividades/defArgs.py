"""
*args and **kwagrs

"""

def valores (*args):
    print(args)

lista =  [1,3,5,66,0]
lista2 =  [1,3,5,66,0]

valores(*lista,*lista2)