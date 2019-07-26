# importação da biblioteca para selecionar coisas aleatorias
import random
# Gera numeros aleatórios
adivinha_num=random.randint(1,1000)
# define o número de tentativas que vc tem
for i in range(1,100):
chute = int(input("Digite seu chute:"))
# limita o tamanho do número que vc pode chutar
if(chute < 1 or chute > 1000):
  print("a sua tentativa pode ser de 1 a 1000")
  continue
# diz se o chute esta certo, menor, ou maior
if(adivinha_num == chute):
  print("Parabéns! Você acertou!")
  print("Jogue de novo, você é um bom jogador!!")
  break
elif(chute>adivinha_num):
  print("Seu chute foi maior que o número secreto!")
elif(chute<adivinha_num):
  print("Seu chute foi menor que o número secreto!")