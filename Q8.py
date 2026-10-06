def kth_factor(n,k):
    factors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factors.append(i)

            if i!=n//i:
                factors.append(n//i)
    factors.sort()

    if k<=len(factors):
        return factors[k-1]
    else:
        return -1
n1=12
k1=3
n2=1
k2=1
n3=12
k3=6
n4=12
k4=7
n5=36
k5=5
print(kth_factor(n1,k1))
print(kth_factor(n2,k2))
print(kth_factor(n3,k3))
print(kth_factor(n4,k4))
print(kth_factor(n5,k5))