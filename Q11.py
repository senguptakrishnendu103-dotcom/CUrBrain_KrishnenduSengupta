def modularadd(arr):
    MOD=10**9+7
    result=0

    for i in arr:
        result=(result+i)%MOD
    return result

print(modularadd([1000000000, 1000000000, 1000000000]))
print(modularadd([1, 2, 3, 4]))
print(modularadd([]))
print(modularadd([1000000007]))
print(modularadd([0,0,0]))