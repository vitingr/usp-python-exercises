numero = input("Digite um número inteiro: ")
possui_adjacente = False

for i in range(len(numero) - 1):
  if numero[i] == numero[i + 1]:
    possui_adjacente = True
    break

if possui_adjacente:
    print("sim")
else:
    print("não")