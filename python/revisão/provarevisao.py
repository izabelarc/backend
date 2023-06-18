'''Faça um programa em Python que, utilizando estruturas de repetição, calcule a média de idade dos alunos 
de uma turma. O programa deve pedir ao usuário a quantidade de alunos na turma e, em seguida, solicitar a idade 
de cada um. O programa deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para 
realizar a soma das idades. Ao final, o programa deve exibir a média de idade da turma.'''

alunos = int(input("Digite a quantidade de alunos: "))
soma = 0
contador = 0

while contador < alunos:
    for i in range(alunos):
        idade = int(input("Digite a idade do aluno: "))
        soma+=idade
        media=soma/alunos
        contador+=1
    
print("A média de idade da turma é: ", media)