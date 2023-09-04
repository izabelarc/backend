
def calcular_media(notas):
    if len(notas) == 0:
        return 0  
    soma = sum(notas)
    media = soma / len(notas)
    return media


def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


notas = []
quantidade_notas = int(input("Quantas notas você deseja inserir? "))
for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = calcular_media(notas)


situacao = verificar_situacao(media)


print(f"Sua média é: {media}")
print(f"Situação: {situacao}")