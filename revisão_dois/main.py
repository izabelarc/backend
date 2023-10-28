def leitor(*textos: tuple) -> list[any]:
    valores_lidos = []
    
    for texto in textos:
        valor = input(texto + ": ")
        valores_lidos.append(valor)
        
        return valores_lidos
        
    leitor(
        "Informe seu nome",
        "Informe seu endereço",
        "Informe seu cpf",
        "Informe seu email",
        "Informe seu telefone"
    )