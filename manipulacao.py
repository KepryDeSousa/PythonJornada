"""file = open('abnt.txt','w+')
#w Escrita, + leitura

file.write('Linha 1 \n')
file.write('Linha 2 \n')
file.write('Linha 3 \n')

#write serve para escrever no arquivo
file.seek(0,0)
# seek(inicial, final)

#quando estamos modificando um arquivo não conseguimos visualizado
#mas usando seek conseguimos ler o arquivo em execução 

for linha in file:
    print(linha);

file.close()"""
try:
    with open('abnt.txt','w+') as file :
        file.write('eu \n')
        file.write('to \n')
        file.write('testando\n ')
        file.seek(0)
    # with é um gerenciador de contexto, ele fecha o arquivo no final
except:
    print('deu ruim')

arq = open('abnt.txt',"r")
for a in arq :
    print(a)