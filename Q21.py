def delete_by_value(arr,target):
    n=len(arr)

    for i in range(n):
        if arr[i]==target:
            for j in range(i,n-1):
                arr[j]=arr[j+1]
            arr.pop()
            break
    return arr

arr1=[10,20,30,20,40]
target1=20
delete_by_value(arr1,target1)
print(arr1)
arr2=[5,15]
target2=99
delete_by_value(arr2,target2)
print(arr2)
arr3=[7]
target3=7
delete_by_value(arr3,target3)
print(arr3)
arr4=[]
target4=3
delete_by_value(arr4,target4)
print(arr4)
arr5=[4,4,4]
target5=4
delete_by_value(arr5,target5)
print(arr5)