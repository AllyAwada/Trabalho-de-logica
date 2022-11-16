import time #Trabalhar com tempo
import random #Sortear um numero aleatorio
import os #Importar comandos de sistema

dificuldade = int(input('Digite \n 1. fácil \n 2. médio \n 3. difícil \n'))
jogar = input('Para começar digite "S"')

pc = 0
user = 0

def sorteio_facil():
     num1 = random.randint(1,10)
     num2 = random.randint(1,10)
     num3 = random.randint(1,10)
     num4 = random.randint(1,10)
     num5 = random.randint(1,10)
     while num1>0:
          if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
               num1 = random.randint(1,10)
          elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5:
               num2 = random.randint(1,10)
          elif num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
               num3 = random.randint(1,10)
          elif num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
               num4 = random.randint(1,10)
          elif num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
               num5 = random.randint(1,10)
          elif num1 != num2 and num1 != num3 and num1 != num4 and num1 != num5 and num2 != num1 and num2 != num3 and num2 != num4 and num2 != num5 and num3 != num1 and num3 != num2 and num3 != num4 and num3 != num5 and num4 != num1 and num4 != num2 and num4 != num3 and num4 != num5:
               break
     return num1,num2,num3,num4,num5


def sorteio_medio():
     num1 = random.randint(1,50)
     num2 = random.randint(1,50)
     num3 = random.randint(1,50)
     num4 = random.randint(1,50)
     num5 = random.randint(1,50)
     while num1>0:
          if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
               num1 = random.randint(1,50)
          elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5:
               num2 = random.randint(1,50)
          elif num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
               num3 = random.randint(1,50)
          elif num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
               num4 = random.randint(1,50)
          elif num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
               num5 = random.randint(1,50)
          elif num1 != num2 and num1 != num3 and num1 != num4 and num1 != num5 and num2 != num1 and num2 != num3 and num2 != num4 and num2 != num5 and num3 != num1 and num3 != num2 and num3 != num4 and num3 != num5 and num4 != num1 and num4 != num2 and num4 != num3 and num4 != num5:
               break
     return num1,num2,num3,num4,num5

def sorteio_dificil():
     num1 = random.randint(1,100)
     num2 = random.randint(1,100)
     num3 = random.randint(1,100)
     num4 = random.randint(1,100)
     num5 = random.randint(1,100)
     while num1>0:
          if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
               num1 = random.randint(1,100)
          elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5:
               num2 = random.randint(1,100)
          elif num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
               num3 = random.randint(1,100)
          elif num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
               num4 = random.randint(1,100)
          elif num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
               num5 = random.randint(1,100)
          elif num1 != num2 and num1 != num3 and num1 != num4 and num1 != num5 and num2 != num1 and num2 != num3 and num2 != num4 and num2 != num5 and num3 != num1 and num3 != num2 and num3 != num4 and num3 != num5 and num4 != num1 and num4 != num2 and num4 != num3 and num4 != num5:
               break
     return num1,num2,num3,num4,num5

def nov():
     global jogar
     global dificuldade

     jogar = input('Para jogar novamente digite "S"')
     if jogar == 'S':
          dificuldade = int(input('Digite \n 1. fácil \n 2. médio \n 3. difícil \n'))
          tentativas()
     else: 
          print('encerrando o programa')


def tentativas():
     global pc, user
     if dificuldade == 1:
          num1,num2,num3,num4,num5 = sorteio_facil()
          print('Decore os segintes numeros:')
          print("", num1, '\n', num2, '\n', num3, '\n', num4, '\n', num5)
          time.sleep(5)
          os.system('cls')

          resp1 = int(input('Primeiro numero'))
          if resp1 > 10 or resp1 < 1:
               resp1 = int(input('Dê um numero entre 1 e 10'))
          resp2 = int(input('Segundo numero'))
          if resp2 > 10 or resp2 < 1:
               resp2 = int(input('Dê um numero entre 1 e 10'))
          resp3 = int(input('Terceiro numero'))
          if resp3 > 10 or resp3 < 1:
               resp3 = int(input('Dê um numero entre 1 e 10'))
          resp4 = int(input('Quarto numero'))
          if resp4 > 10 or resp4 < 1:
               resp4 = int(input('Dê um numero entre 1 e 10'))
          resp5 = int(input('Quinto numero'))
          if resp5 > 10 or resp5 < 1:
               resp5 = int(input('Dê um numero entre 1 e 10'))

     elif dificuldade == 2:
          num1,num2,num3,num4,num5 = sorteio_medio()
          print('Decore os segintes numeros:')
          print("", num1, '\n', num2, '\n', num3, '\n', num4, '\n', num5)
          time.sleep(5)
          os.system('cls')

          resp1 = int(input('Primeiro numero'))
          if resp1 > 50 or resp1 < 1:
               resp1 = int(input('Dê um numero entre 1 e 50'))
          resp2 = int(input('Segundo numero'))
          if resp2 > 50 or resp2 < 1:
               resp2 = int(input('Dê um numero entre 1 e 50'))
          resp3 = int(input('Terceiro numero'))
          if resp3 > 50 or resp3 < 1:
               resp3 = int(input('Dê um numero entre 1 e 50'))
          resp4 = int(input('Quarto numero'))
          if resp4 > 50 or resp4 < 1:
               resp4 = int(input('Dê um numero entre 1 e 50'))
          resp5 = int(input('Quinto numero'))
          if resp5 > 50 or resp5 < 1:
               resp5 = int(input('Dê um numero entre 1 e 50'))

     elif dificuldade == 3:
          num1,num2,num3,num4,num5 = sorteio_dificil()
          resp1 = int(input('Primeiro numero'))
          if resp1 > 100 or resp1 < 1:
               resp1 = int(input('Dê um numero entre 1 e 100'))
          resp2 = int(input('Segundo numero'))
          if resp2 > 100 or resp2 < 1:
               resp2 = int(input('Dê um numero entre 1 e 100'))
          resp3 = int(input('Terceiro numero'))
          if resp3 > 100 or resp3 < 1:
               resp3 = int(input('Dê um numero entre 1 e 100'))
          resp4 = int(input('Quarto numero'))
          if resp4 > 100 or resp4 < 1:
               resp4 = int(input('Dê um numero entre 1 e 100'))
          resp5 = int(input('Quinto numero'))
          if resp5 > 100 or resp5 < 1:
               resp5 = int(input('Dê um numero entre 1 e 100'))


     if num1 == resp1 and num2 == resp2 and num3 == resp3 and num4 == resp4 and num5 == resp5:
          print('----------------------')
          print('Parabens Você ganhou')
          user = user + 1 
          print('Placar geral')
          print('Pc:', pc, '   User:', user)
          time.sleep(0.3)
          nov()
     else:
          print('----------------------')
          print('O pc ganhou')
          print('O certo é', '\n', num1, "\n", num2, "\n", num3, "\n", num4, "\n", num5, "\n")
          pc = pc + 1
          print('Placar geral')
          print('Pc', pc, '   User', user)
          time.sleep(0.3)
          nov()

while jogar == 'S':
     tentativas()