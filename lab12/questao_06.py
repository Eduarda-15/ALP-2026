import time
import random
N = random.randint(2, 10)
time.sleep(N)
print("AGORA!")
tempo0 = time.time()
input()
tempo1 = time.time()
print(f'Se passaram {tempo1-tempo0} segundos! (^o^)')
