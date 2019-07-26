# importação da biblioteca para selecionar coisas aleatorias
import random
#lista das palavras a serem sorteadas
show = ["banana","melancia", "abacaxi", "manga"]
# seleciona aleatoriamente as palavras
aleatorio =random.choice(show)
# condições para entrar no laço
acertos = False
enforcou=False
# laço
while(not acertos and not enforcou):
 index = 0
 digitadas = []
# pega a letra digitada pelo usuario
 chances=input("digite seu chute:").lower().strip()
# indica se o chute esta em alguma letra da palavra secreta
 for x in aleatorio:
   if(chances == x):
     print("Letra {} encontrada na posicao {}".format(chances,index))
   index +=1
print("Fim do jogo")