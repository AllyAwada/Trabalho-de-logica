import time #Trabalhar com tempo
import random #Sortear um numero aleatorio
import os #Importar comandos de sistema



pc = 0
user = 0

def manual():
     print('Manual \n O jogo da memoria 2.0 tem o diferencial pois possue 3 dificudades \n 1 = fácil onde os numeros sorteados serão entre 1 e 10 e quando o usuario ganha ele ganha apenas 1 ponto e quando o pc ganha ele recebe 7 pontos \n 2 = média onde os numeros sorteados serão entre 1 e 50 e quando o usuario ganhar ele ganha 5 pontos e quando o pc ganha ele recebe 5 pontos \n 3 = difícil onde os numeros sorteados serão entre 1 e 100 e quando o usuario ganhar ele ganha 7 pontos e quando o pc ganha ele recebe apenas 1 ponto')

def sorteio(Numeros):
     num1 = random.randint(1,Numeros)
     num2 = random.randint(1,Numeros)
     num3 = random.randint(1,Numeros)
     num4 = random.randint(1,Numeros)
     num5 = random.randint(1,Numeros)
     while num1>0:
          if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
               num1 = random.randint(1,Numeros)
          elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5:
               num2 = random.randint(1,Numeros)
          elif num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
               num3 = random.randint(1,Numeros)
          elif num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
               num4 = random.randint(1,Numeros)
          elif num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
               num5 = random.randint(1,Numeros)
          elif num1 != num2 and num1 != num3 and num1 != num4 and num1 != num5 and num2 != num1 and num2 != num3 and num2 != num4 and num2 != num5 and num3 != num1 and num3 != num2 and num3 != num4 and num3 != num5 and num4 != num1 and num4 != num2 and num4 != num3 and num4 != num5:
               break
     return num1,num2,num3,num4,num5


def nov():
     global jogar
     global dificuldade

     jogar = input('Para jogar novamente digite "S"')
     if jogar == 'S' or jogar == 's':
          man = input('Para ver o manual digite M caso o contrario precione enter')
          if man == 'M' or man == 'm':
               manual()
          dificuldade = int(input('Escolha uma dificuldade \n 1. fácil \n 2. médio(Recomendado) \n 3. difícil \n'))
          tentativas()
     else: 
          print('encerrando o programa')

def respostas(Max):
     resp1 = int(input('Primeiro numero'))
     if resp1 > Max or resp1 < 1:
          resp1 = int(input('Dê um numero entre 1 e', max))
     resp2 = int(input('Segundo numero'))
     if resp2 > Max or resp2 < 1:
          resp2 = int(input('Dê um numero entre 1 e', max))
     resp3 = int(input('Terceiro numero'))
     if resp3 > Max or resp3 < 1:
          resp3 = int(input('Dê um numero entre 1 e', max))
     resp4 = int(input('Quarto numero'))
     if resp4 > Max or resp4 < 1:
          resp4 = int(input('Dê um numero entre 1 e', max))
     resp5 = int(input('Quinto numero'))
     if resp5 > Max or resp5 < 1:
          resp5 = int(input('Dê um numero entre 1 e', max))
     return resp1, resp2, resp3, resp4, resp5

def tentativas():
     global pc, user
     if dificuldade == 1:
          num1,num2,num3,num4,num5 = sorteio(10)
          print('Decore os segintes numeros:')
          print("", num1, '\n', num2, '\n', num3, '\n', num4, '\n', num5)
          time.sleep(5)
          os.system('cls')
          resp1, resp2, resp3, resp4, resp5 = respostas(10)

     elif dificuldade == 2:
          num1,num2,num3,num4,num5 = sorteio(50)
          print('Decore os segintes numeros:')
          print("", num1, '\n', num2, '\n', num3, '\n', num4, '\n', num5)
          time.sleep(5)
          os.system('cls')
          resp1, resp2, resp3, resp4, resp5 = respostas(50)

     elif dificuldade == 3:
          num1,num2,num3,num4,num5 = sorteio(100)
          print('Decore os segintes numeros:')
          print("", num1, '\n', num2, '\n', num3, '\n', num4, '\n', num5)
          time.sleep(5)
          os.system('cls')
          resp1, resp2, resp3, resp4, resp5 = respostas(100)

     if num1 == resp1 and num2 == resp2 and num3 == resp3 and num4 == resp4 and num5 == resp5:
          print('----------------------')
          print('Parabens Você ganhou')
          if dificuldade == 1:
               user = user + 1
          elif dificuldade == 2:
               user = user + 5
          elif dificuldade == 3:
               user = user + 7
          print('Placar geral')
          print('Pc:', pc, '   User:', user)
          time.sleep(0.3)
          nov()
     else:
          print('----------------------')
          print('O pc ganhou')
          print('O certo é', '\n', num1, "\n", num2, "\n", num3, "\n", num4, "\n", num5, "\n")
          if dificuldade == 1:
               pc = pc + 7
          elif dificuldade == 2:
               pc = pc + 5
          elif dificuldade == 3:
               pc = pc + 1
          print('Placar geral')
          print('Pc', pc, '   User', user)
          time.sleep(0.3)
          nov()

man = input('Para ver o manual digite M caso o contrario precione enter')
if man == 'M' or man == 'm':
     manual()

dificuldade = int(input('Escolha uma dificuldade \n 1. fácil \n 2. médio(Recomendado) \n 3. difícil \n '))
jogar = input('Para começar digite "S" \n ')

while jogar == 'S' or jogar == 's':
     tentativas()