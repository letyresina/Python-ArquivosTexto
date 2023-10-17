'''
    Exercício 6:
    Um professor armazena em um arquivo de texto uma listagem das notas dos alunos na disciplina, 
    onde cada linha contém o nome do aluno e os valores de quatro notas.
    Escreva um programa que leia esse arquivo e calcule a média de cada aluno.
'''

with open('exercicio6/notas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        lista = linha.split()
        notas = lista[-1:-5:-1]
        print('-' * 50)
        print(f'\nNotas: {notas}')
        soma = 0
        for n in notas:
            soma += float(n)
        media = soma / 4
        print(f'{media:.2f}')