def reverse_segment(arr,start,end):
    left=start
    right=end

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(reverse_segment([10,20,30,40,50,60],1,4))
print(reverse_segment([1,2,3,4],0,3))
print(reverse_segment([7],0,0))
print(reverse_segment([1,2,3,4,5],2,4))
print(reverse_segment([1,2,3,4,5],0,2))