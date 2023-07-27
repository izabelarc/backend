# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = list(range(10))
vetor2 = list(range(11,21))
vetor3 = list(range(22,32))
vetor4=[]

for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(vetor4)