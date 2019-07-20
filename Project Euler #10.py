import time
import math
start = time.time()
primelist= [2]

def primefinder(number):
    prime = [True] * (number+1)
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y*y, number + 1,y+y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)

primefinder(2000000)

print(sum(primelist))
end = time.time()
print(end - start)
