import time

def contagem_regressiva(num):
    for i in range(num,-1,-1):
        print(i)
        time.sleep(1)
contagem_regressiva(10)
