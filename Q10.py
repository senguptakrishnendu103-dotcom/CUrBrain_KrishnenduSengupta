def countprimes(n):
    if n<=2:
        return 0

    prime=[True]*n
    prime[0]=prime[1]=False
    for i in range(2,int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i,n,i):
                prime[j]=False

    return sum(prime)
print(countprimes(10))    
print(countprimes(2))
print(countprimes(0))
print(countprimes(3))
print(countprimes(30))    