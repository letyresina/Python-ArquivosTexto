'''
    Exercício 1:
    Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada 
    linha).
'''

# Abrindo arquivo
arquivo = open("exercicio1/arquivoTexto.txt", "w")

for i in range(10):
    num = int(input("Informe um número inteiro qualquer: "))
    arquivo.write(str(num) + '\n')

arquivo.close()