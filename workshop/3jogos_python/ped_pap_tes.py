from random import randint
random_word = randint(0,2)

print("Veja suas opções: ")
print("1- Pedra")
print("2- Papel")
print("3- Tesoura")
escolha = input("Digite o número da sua escolha: ")

while escolha != random_word or escolha == random_word:
    if escolha.isdigit() and escolha >= "1" and escolha <= "3":
        while escolha != random_word or escolha == random_word:
            try:
                if random_word == 0:
                    print("O computador escolheu: Pedra.")
                    if escolha == 1:
                        print("Você também escolheu Pedra. Empatou!")
                    elif escolha == 2:
                        print("Você escolheu Papel. Você ganhou!")
                    else:
                        print("Você escolheu Tesoura. O computador ganhou!")
                    break
                elif random_word == 1:
                    print("O computador escolheu: Papel.")
                    if escolha == 2:
                        print("Você também escolheu Papel. Empatou!")
                    elif escolha == 3:
                        print("Você escolheu Tesoura. Você ganhou!")    
                    else:
                        print("Você escolheu Pedra. O computador ganhou!")
                    break
                else:
                    print("O computador escolheu: Tesoura.")
                    if escolha == 3:
                        print("Você escolheu Tesoura.Empatou!")
                    elif escolha == 1:
                        print("Você escolheu Pedra. Você ganhou!")
                    else:
                        print("Você escolheu Papel. O computador ganhou!")
                    break
            except:
                print("Você não digitou um número válido.")
        break            
    else:
            escolha = input("Você não digitou um número ou não escolheu um número presente no menu. Digite o número da opção que deseja: ")
print("Fim do jogo!")