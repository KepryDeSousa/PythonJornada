"""
Conjuntos ou Sets, eles devem ter valores unicos
                    por não terem index, ele não podem ser acessados
                    não existe ordem

"""
s = {1,2,3,45,6}
print(type(s))
s1 = [23]
print(type(s1))
s2 = {'num': '23'}
print(type(s2))

"operações"
s1 = {1,2,3,4,5}
s2 = {6,8,9,5,4}
s4 = s1 | s2;"union"
s3 = s1  & s2; "Interception"
s3 = s1 - s2; "dif, no set da esquerda que é unico em relação ao da direita"
s3 = s2 - s1;
s3 = s1 ^ s2;'dif simetrico, valores diferentes em ambos sets'
print(s4)