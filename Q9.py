import math
def nextprime(n):
    x=max(2,n+1)

    while True:
        prime=True

        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                prime=False
                break

        if prime:
            return x
        x+=1
print(nextprime(14))
print(nextprime(0))
print(nextprime(1))
print(nextprime(2))
print(nextprime(17))