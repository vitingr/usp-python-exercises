valor = int(input("Digite o valor de n: "))
if valor != 0:
  for contador in range(1, valor, 1):
    valor *= contador
else:
  valor = 1
print(valor)