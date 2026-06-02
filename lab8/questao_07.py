degrau = 1
while True:
    print("--> Jogo das Escadas <--")
    print("Degrau atual:", degrau)
    passos = int(input("Digite um número de passos (1-6) ou 0 para sair: "))
    if passos == 0:
        print("Você desistiu do jogo! :(")
        break
    if passos < 1 or passos > 6:
        print("Valor inválido, tente novamente!")
        continue
    novo_degrau = degrau + passos
    print("Você andou passos", passos, "e chegou no degrau", novo_degrau)
    if novo_degrau % 3 == 0:
        novo_degrau -= 1
        print("Volte 1 degrau!")
    elif novo_degrau % 5 == 0:
        novo_degrau += 1
        print("Avance mais 1 degrau!")
    elif novo_degrau % 7 == 0:
        novo_degrau += 4
        print("Avance mais 4 degraus!")
    elif novo_degrau % 11 == 0:
        novo_degrau = 1
        print("Volte para o início...")
    degrau = novo_degrau
    if degrau >= 100:
        print("Parabens! Você chegou no degrau", degrau,"Você venceu!!")
        break
