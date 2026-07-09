import random
def roleta():
    num = random.randint(1, 36)
    if num % 2 ==0:
        return num,"Preto"
    else:
        return num,"Vermelho"
print(roleta())
