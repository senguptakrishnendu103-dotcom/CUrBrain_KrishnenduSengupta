def shortest_subarray(arr,target):
    n=len(arr)
    min_length=float('inf')
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=arr[j]
            if current_sum>=target:
                length=j-i+1
                min_length=min(min_length,length)
                break
    if min_length==float('inf'):
        return 0
    return min_length

arr1=[2,3,1,2,4,3]
target1=7
print(shortest_subarray(arr1,target1))
arr2=[1,1,1]
target2=10
print(shortest_subarray(arr2,target2))
arr3=[5]
target3=5
print(shortest_subarray(arr3,target3))
arr4=[1,2,3,4,5]
target4=11
print(shortest_subarray(arr4,target4))
arr5=[]
target5=3
print(shortest_subarray(arr5,target5))