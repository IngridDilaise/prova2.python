import random

numero_secreto=random.randint(1,50)
for i in range(1,20):
  chute = int(input("Digite seu chute:"))
  
  if(chute < 1 or chute > 50):
    print("a sua tentativa pode ser de 1 a 50")
    continue

  acertou =numero_secreto == chute
  maior = chute>numero_secreto
  menor = chute<numero_secreto

  if(acertou):
    print("Voce acertou")
    break
  elif(maior):
    print("o seu chute foi maior que o numero escolhido!")
  elif(menor):
    print("o seu chute foi menor que o numero escolhido")
print("fim do jogo")