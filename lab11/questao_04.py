import random
ponto1 = 0
ponto2 = 0
rodada = 1
while ponto1 < 50 and ponto2 < 50:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print("==> RODADA",rodada, "<==")
    palp1 = int(input(f'Jogador 1 (pontos: {ponto1}) : Qual o seu palpite para a soma dos dados? > '))
    palp2 = int(input(f'Jogador 2 (pontos: {ponto2}) : Qual o seu palpite para a soma dos dados? > '))
    print("Rolando os dados...")
    print("Dado 1: ",dado1)
    print("Dado 2: ",dado2)
    soma = dado1 + dado2
    p1 = abs(soma - palp1)
    p2 = abs(soma - palp2)
    if p1 < p2:
        print("Resultado: Jogador 1 ganhou 5 pontos!!")
        ponto1 += 5
    elif p2 < p1:
        print("Resultado: Jogador 2 ganhou 5 pontos!!")
        ponto2 += 5
    else:
        print("Resultado: EMPATE! Cada um ganha 2 pontos!")
        ponto1 += 2
        ponto2 += 2
    rodada += 1
print("==> FIM DE JOGO <==")
ven1 = "Jogador 1"
ven2 = "Jogador 2"
if ponto1 >= 50:
    print("O vencedor é", ven1)
else:
    print("O vencedor é", ven2)
