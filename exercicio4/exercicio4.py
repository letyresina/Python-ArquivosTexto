'''
    Exercício 4:
    Solicite ao usuário diversos números inteiros (até que seja digitado o número zero). Armazene os 
    números pares em um arquivo e os números ímpares em outro arquivo.
'''

arquivoPar = open("exercicio4/arquivoPar.txt", "w")

arquivoImpar = open("exercicio4/arquivoImpar.txt", "w")

while True:
    num = int(input('Digite um numero para ser armazenado ou digite "0" para sair: '))
    if num == 0:
        break
    if num % 2 == 0:

        arquivoPar.write(f"{num} \n")
    else:
        arquivoImpar.write(f"{num} \n")

arquivoPar.close()
arquivoImpar.close()