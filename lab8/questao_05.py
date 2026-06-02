conta = 0
while True:
    print("--> Cardápio <--")
    print("1. Açaí - R$ 18.00")
    print("2. Pão de queijo - R$ 05.00")
    print("3. Coxinha - R$ 03.00")
    print("4. Picolé - R$ 06.00")
    print("5. Fechar conta.")
    opcao = int(input("Digite o número da sua opção: "))
    if opcao == 5:
        print("Valor total:", conta)
        print("Volte sempre!")
        break
    elif opcao == 1:
        conta += 18
        print("Açaí adicionado!")
    elif opcao == 2:
        conta += 5
        print("Pão de queijo adicionado!")
    elif opcao == 3:
        conta += 3
        print("Coxina adicionada!")
    elif opcao == 4:
        conta += 6
        print("Picolé adicionado!")
    else:
        print("Opção inválida!")
        continue


