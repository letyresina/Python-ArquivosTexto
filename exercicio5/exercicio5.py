'''
    Exercício 5:
    Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo 
    arquivo, colocando-os em ordem crescente.
'''

arquivoOrdemCrescente = open("exercicio5/arquivoOrdemCrescente.txt", "w")

lista = []

with open("exercicio4/arquivoPar.txt", "r") as arquivoPar:
    for linha in arquivoPar:
        lista.append(int(linha))

with open("exercicio4/arquivoImpar.txt", "r") as arquivoImpar:
    for linha in arquivoImpar:
        lista.append(int(linha))

print(lista)

lista.sort()

print(lista)

#escreverVariavel = lista.split(' ')

for i in lista:
    arquivoOrdemCrescente.write(f"{i} \n")

arquivoOrdemCrescente.close()