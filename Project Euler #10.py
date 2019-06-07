import math
import time

primelist = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]


number = 1999999

start = time.time()

def primefinder(number):
    for y in range(103, number + 1,2):
        prime = True
        for x in primelist:
            if y % x == 0:
                prime = False
                break
            if x > math.sqrt(y):
                break
        if prime == True:
            primelist.append(y)


primefinder(int(number))

end = time.time()
primelist.insert(0,2)
print(sum(primelist))
print(end - start)



