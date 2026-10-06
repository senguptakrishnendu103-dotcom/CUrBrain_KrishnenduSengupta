def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def arr_gcd(arr):
    result=arr[0]

    for num in arr[1:]:
        result= gcd(result,num)
    return result

arr1=[24, 36, 48] 
arr2=[33, 44, 55, 66] 
arr3=[17] 
arr4=[12, 18, 24, 30] 
arr5=[1, 7, 14, 28] 
print(arr_gcd(arr1))
print(arr_gcd(arr2))
print(arr_gcd(arr3))
print(arr_gcd(arr4))
print(arr_gcd(arr5))