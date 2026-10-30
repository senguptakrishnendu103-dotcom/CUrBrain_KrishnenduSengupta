def smallest_absolute(arr):
        smallest=arr[0]
        for num in arr:
            if abs(num)<abs(smallest):
                smallest=num
        return smallest
arr1=[10,-5,-2,4,2]
arr2=[-3,3] 
arr3=[0,-1,1]
arr4=[7,-7,4] 
arr5=[5,-2,2,-1]
print(smallest_absolute(arr1 ))
print(smallest_absolute(arr2))
print(smallest_absolute(arr3 ))
print(smallest_absolute(arr4))
print(smallest_absolute(arr5 ))