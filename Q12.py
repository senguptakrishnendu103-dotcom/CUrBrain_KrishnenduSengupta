def moduloPower(b,e,MOD):
    
    result=1%MOD

    for i in range(e):
        result=(result*b)%MOD
    return result

print(moduloPower(2, 10, 1000))
print(moduloPower(7, 0, 13))
print(moduloPower(9, 1, 7))
print(moduloPower(3, 4, 1))
print(moduloPower(0, 5, 11))
