import random
import time
N = random.randint(0, 10)
volta = 0
for i in range(N):
    volta += 1
    print(f'Volta {volta}: Mais uma volta!')
    time.sleep(1)
