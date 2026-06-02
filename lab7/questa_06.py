print("Cardápio!")
print("1. Açaí 300ml - R$ 12")
print("2. Coxinha - R$ 6,50")
print("3. Picolé - R$ 3,50")
print("4. Fechar a conta")
conta = 0
while True:
    num = int(input("Digite um número:"))
    if num == 1:
        conta += 12
        print("Total: R$12,00")
    if num == 2:
        conta += 6.50
        print("Total: R$6,50")
    if num == 3:
        conta += 3.50
        print("Total: R$3,50")
    if num == 4:
        conta += 0
        print("Total: R$00,00")
    break

