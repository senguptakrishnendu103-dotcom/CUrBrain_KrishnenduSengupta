def r_e_z(n):
    digits=[]

    while n>0:
        digit=n%10

        if digit%2==0:
            digit=0
        
        digits.append(digit)
        n=n//10
    digits.reverse()
    return digits

print(r_e_z(258))
print(r_e_z(12345))
print(r_e_z(2468))
print(r_e_z(13579))
print(r_e_z(1002))