import time
entrada = int(input('Quanto tempo de pausa?'))
tempo0 = time.time()
time.sleep(entrada * 2)
tempo1 = time.time()
print('Você esperou', int(tempo1 - tempo0), 'segundos')

#segundo código
soma = 0
fim = int(input())
for i in range(1, fim, 2):
    soma = soma + i
print("Soma:", soma)

#terceiro código
import datetime
hoje = datetime.datetime.now()
ano = int(input('Que ano você nasceu?'))
print(hoje.year, ano, hoje.year-ano)
