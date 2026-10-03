def reverse_double(n):
    sign=-1 if n<0 else 1
    n=abs(n)

    reverse=0
    while n>0:
        digits=n%10
        reverse = reverse * 10 + digit
        n=n//10
    reverse = reverse * sign
    return reverse*2
print(reverse_double(123))
print(reverse_double(-45))
print(reverse_double(0))
print(reverse_double(1200))
print(reverse_double(9))