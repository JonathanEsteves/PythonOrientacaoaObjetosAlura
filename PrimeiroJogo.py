import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
print("Qual nível de dificuldade do jogo")
print("(1) Fácil (2) Médio (3) Difícil: ")
 # Definindo o nível de dificuldade do jogo
nivel=int(input("Defina o seu nível: "))

if (nivel == 1):
    total_de_tentativas = 15
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1,total_de_tentativas + 1):
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))
  chute_str = input("Digite o seu número entre 1 e 100: ")
  print("Você digitou: ", chute_str)
  chute = int(chute_str)
# primeira condição if sobre limite de número aceito
  if(chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

  acertou = numero_secreto == chute
  chutemaior = chute > numero_secreto
  chutemenor = chute < numero_secreto
# bloqueando com o loop (break) ao usuário acertar o número secreto
  if(acertou):
    print("Você acertou!")
    break
  else:
   # utilizando (if) & (elif) na condição de checar o número for maior ou menor do número secreto
   if(chutemaior):
     print("Você errou! O seu chute foi maior do que o número secreto.")
   elif(chutemenor):
       print("Você errou! Seu chute foi menor que o número secreto.")
   print("Fim de jogo")




