while True:
    valor = int(input("Digite o valor que deseja sacar: "))
    if valor <= 0:
        print("Valor indevido para sacar! Digite outro valor.")
        continue
    if valor % 10 != 0 or valor == 10 or valor == 30:
        print("Notas indisponíveis para saque!")
        print("Notas disponíveis: R$20, R$ 50, R$100")
        continue
    print("saque realizado com sucesso!")
    break
