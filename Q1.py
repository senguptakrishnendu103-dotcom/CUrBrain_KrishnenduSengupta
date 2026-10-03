def even_digits(n):
    n=abs(n)

    if n==0:
        digits=1
    else:
        digits=0
        while n>0:
            n=n//10
            digits+=1
    return digits%2==0

print(even_digits(1234))
print(even_digits(12345))
print(even_digits(0))
print(even_digits(-100000))
print(even_digits(-7))
