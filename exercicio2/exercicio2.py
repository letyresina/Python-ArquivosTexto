'''
    Exercício 2:
    Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório 
    de todos os números contidos no arquivo.
'''

arquivo = open("exercicio1/arquivoTexto.txt", "r")

somatorio = 0

for linha in arquivo:
    linha = int(linha)
    somatorio += linha

print(somatorio)