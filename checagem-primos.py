numero = int(input("Digite um número inteiro: "))

if numero > 1:
  for i in range(2, numero):
    if (numero % i) == 0:
      print("não primo")
      break
  else:
    print("primo")
else:
  print("não primo")
  