#A
for i in range(5):
    print(i)

#B
for x in range(1,10,2):
    print(x)

#C
for n in range(5,0,-1):
    print(n)

#D
soma = 0
for i in range(0,10,5):
    soma += i
    print(i)
    print(soma)

#E
soma = 0
for i in range(5,10):
    print(i)
    print(soma)
    if i % 2 ==0:
        soma+=i

#F
n = 100
for i in range(100,50,-10):
    sub = n-i
    print(i)
    print(sub)
    
#G
soma = 0
for i in range(10):
    if i ==3:
        continue
    if i ==7:
        break
    soma += i
    print(i, soma)
