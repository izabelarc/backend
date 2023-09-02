from bibliotecas.pessoa import Pessoa 

pessoa1 = Pessoa("José", 12, "masculino")
pessoa2 = Pessoa(
    nome="Maria",
    idade= 25,
    sexo="feminino",
)

pessoa1.envelhcer()
pessoa2.envelhcer()
pessoa1.identidade()
print()
pessoa2.identidade()

