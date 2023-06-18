'''Crie um algoritmo que solicite ao usuário digitar um número. 
Em seguida, calcule a tabuada deste número até 10 e exiba cada uma das multiplicações na tela.'''
numero = int(input("Digite um número: "))
for i in range(1,11):
    multiplicação = i*numero
    # print(i, "x", numero, "=", multiplicação)
    print(f'{i} x {numero} = {multiplicação}')