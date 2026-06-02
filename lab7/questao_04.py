import random
chances = 5
numero = random.randint(1, 10)
while chances > 0:
    tentativa = input(f"Qual o número secreto? Você tem {chances} chances")
    chances -= 1
    if tentativa == numero:
        print("Você acertou!!")
        break
#Essa questao eu tive muitas dúvidas.
