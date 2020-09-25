from time import sleep
import random
print('Olá,seja bem vindo ao jogo de pedra papel e tesoura')
print('''Escolha entre pedra papel ou tesoura
[1]pedra
[2]papel
[3]tesoura''')
#Vai aleatoriamente escolher um numero entre 1 a 3
bot = random.randint(1,3)
jogador = int(input('escolher: '))
print('JO')
sleep(1.0)
print('KEN')
sleep(1.0)
print('PO')
# Tesoura X Papel
if bot == 2 and jogador == 3:
    print('Jogador escolheu: tesoura')
    sleep(1.0)
    print('Bot escolheu: papel')
    print('Jogador ganhou')
# Papel X Tesoura
elif jogador == 2 and bot == 3:
    print('Jogador escolheu: papel')
    sleep(1.0)
    print('Bot escolheu: tesoura')
    print('Bot ganhou')
# Pedra X Papel
elif jogador == 1 and bot == 2:
    print('Jogador escolheu: pedra')
    sleep(1.0)
    print('Bot escolheu: papel')
    print('Bot ganhou')
# Papel X Pedra
elif jogador == 2 and bot == 1:
    print('Jogador escolheu: Papel')
    sleep(1.0)
    print('Bot escolheu: pedra')
    print('Jogador ganhou')
# Pedra X Tesoura
elif jogador == 1 and bot == 3:
    print('Jogador escolheu: Pedra')
    sleep(1.0)
    print('Bot escolheu : tesoura')
    print('Jogador ganhou')
# Caso de empate
elif jogador == bot:
    print('Houve um empate,ninguem perdeu mas tambem ninguem ganhou.')
else:
    print('Você digitou um comando errado,por favor tente novamente')
