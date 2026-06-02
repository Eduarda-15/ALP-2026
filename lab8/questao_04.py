soma = 0
num = int(input("Digite um número: "))
while num != 0:
    if num < 0:
        num = int(input("Digite um número: "))
        continue
    soma += num
    if num == 0:
        break
    if soma > 100:
        break
    num = int(input("Digite um número: "))
print("Soma Total: ", soma)
