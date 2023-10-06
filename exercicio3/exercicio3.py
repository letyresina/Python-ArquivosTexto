'''
    Exercício 3:
    Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário 
    grave diversos caracteres nesse arquivo até que seja digitado o caractere “0” (zero).
'''

arquivo = open("exercicio3/arquivo.txt", "a")

while True:
    num = int(input("Digite qualquer número inteiro ou zero para sair do programa: "))
    if num == 0:
        break
    arquivo.write(f"{num} \n")

arquivo.close()