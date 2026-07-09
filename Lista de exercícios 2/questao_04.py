#Primeiro código
import random
import time

inicio = time.time()
print("Preparando envio...")
time.sleep(random.randint(1, 3))
print("Mensagem enviada!")
fim = time.time()
print("Enviou demorou", int(inicio-fim), "segundos")

#Segundo código
import random

for i in range(5):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    diferenca = abs(dado2-dado1)
    if diferenca == 0:
        break

#Terceiro código
import datetime
hoje = datetime.datetime.now()
resposta = input('Incluir ano? (s/n)')
if resposta == 's':
    print(f"{hoje.day}/{hoje.month}/{hoje.year}")
else:
    print(f"{hoje.day}/{hoje.month}")
