def reverse_palindrome(n):
    org=n
    temp=abs(n)
    reverse=0

    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10

    if n>=0 and org==reverse:
        return org
    else:
        if n<0:
            reverse=-reverse
        return n+reverse
print(reverse_palindrome(121))    
print(reverse_palindrome(123))
print(reverse_palindrome(0))
print(reverse_palindrome(-45))
print(reverse_palindrome(120))
