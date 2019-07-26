import random

pal_secreta=["matematica","macaco"]
escolha=random.choice(pal_secreta)

acertou_letra=False
errou_letra=False

while(not acertou_letra and not errou_letra):
  index=0
  letra=input("digite uma letra:").lower().strip()
  for i in escolha:
    if(chute==i):
       print("letra {} encontrada na posicao {}".format(letra,index))
       index+=1
    elif(letra!=i):
       print("letra errada")
print("FIM")



