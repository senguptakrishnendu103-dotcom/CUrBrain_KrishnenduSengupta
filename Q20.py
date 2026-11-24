def replace_wrs(arr):
    total=0

    for i in range(len(arr)-1,-1,-1):
        temp=arr[i]
        arr[i]=total
        total+=temp
    return arr
arr1=[10,4,8,3]
replace_wrs(arr1)
print(arr1)
arr2=[5]
replace_wrs(arr2)
print(arr2)
arr3=[]
replace_wrs(arr3)
print(arr3)
arr4=[-2,5,-1]
replace_wrs(arr4)
print(arr4)
arr5=[1,2,3,4]
replace_wrs(arr5)
print(arr5)