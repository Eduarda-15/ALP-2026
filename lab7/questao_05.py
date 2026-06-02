import random
chances = 5
cont_erro = 0
numero = random.randint(1, 10)
while chances > 0:
    tentativa = int(input(f"Qual o número secreto? Você tem {chances} chances"))
    chances -= 1
    if tentativa > numero:
        print("O número é menor que sua tentativa!")
    else:
        print("O número é maior que sua tentativa!")
    if tentativa == numero:
        print("Você acertou!!")
        break
else:
    print("Suas chances acabaram!")
    
