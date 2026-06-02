#Percebi que quando erra, o código de fato volta para o início.
#Mas as chances diminuem de acordo com as vezes que você erra.
#Quando acerta a palavra, o print do if aparece.
chances = 5
palavra_secreta = 'batata'
while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
