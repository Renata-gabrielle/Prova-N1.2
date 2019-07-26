# importação da biblioteca para selecionar coisas aleatorias
import random
# Força a entrada no while pela primeira vez
valor = True
# roda o jogo quantas vezes vc quiser
while(valor == 1):
dado1=random.randint(1,6)
dado2=random.randint(1,6)
print ("Valor do 1° dado =", dado1)
print ("Valor do 2° dado =", dado2)
print ("soma dos dados =", dado1 + dado2)
#  opção se quer continuar ou n no jogo
valor = int(input ("Aperte 1 para continuar\n Aperte 0 para finalizar"))