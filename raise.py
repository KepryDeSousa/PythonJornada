"excepction suas"

from logging import exception


def divide(n1,n2):
    try:
        return n1/n2
    except  ZeroDivisionError as Error:
        print('Voce tentou dividir por zero')
        raise


print(divide(2,0))