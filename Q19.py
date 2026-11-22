def reversearray(nums,left,right):
    while left<right:
        nums[left], nums[right]=nums[right],nums[left]
        left+=1
        right-=1

def rotate(nums,k):
    n=len(nums)
    k=k%n
    reversearray(nums,0,n-1)
    reversearray(nums,0,k-1)
    reversearray(nums,k,n-1)
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
nums2=[-1,-100,3,99]
k2=2
nums3=[1,2] 
k3=5
nums4=[1]
k4=10

nums5=[1,2,3]
k5=0

rotate(nums1, k1)
print(nums1)


rotate(nums2, k2)
print(nums2)


rotate(nums3, k3)
print(nums3)


rotate(nums4, k4)
print(nums4)


rotate(nums5, k5)
print(nums5)


