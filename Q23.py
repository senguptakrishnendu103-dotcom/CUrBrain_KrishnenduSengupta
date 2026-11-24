def minimum__subarray_sum(arr):
    min_sum=arr[0]
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum+=arr[j]
            if current_sum<min_sum:
                min_sum=current_sum
    return min_sum
arr1=[3,-4,2,-3,5]
print(minimum__subarray_sum(arr1))
arr2=[1,2,3]
print(minimum__subarray_sum(arr2))
arr3=[-1,-2,-3]
print(minimum__subarray_sum(arr3))
arr4=[5]
print(minimum__subarray_sum(arr4))
arr5=[4,-1,-2,1,-5,3]
print(minimum__subarray_sum(arr5))