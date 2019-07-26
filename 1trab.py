#NOME: Ingrid Dilaise Bezerra Maia
#MATRICULA: 20171143000262

#Importar a biblioteca
import random

#entrar no while
valor=True
#condicao
while(valor==1):
  dados=random.randint(1,6)
  print("valor do dado",dados)
  print("aperte para finalizar")
  valor=int(input("aperte o numero de novo, para continuar\n"))
