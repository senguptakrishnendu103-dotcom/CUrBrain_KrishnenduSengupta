def merge(nums1,n,nums2,m):
    i=m-1
    j=n-1
    k=m+n-1
    while j>= 0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
nums1A=[1,2,3,0,0,0]
m1=3
nums2A=[2,5,6]
n1=3
merge(nums1A,n1,nums2A,m1)
print(nums1A)
nums1B=[0]
m2=0
nums2B=[1] 
n2=1
merge(nums1B,n2,nums2B,m2)
print(nums1B)
nums1C=[1]
m3=1
nums2C=[]
n3=0
merge(nums1C,n3,nums2C,m3)
print(nums1C)
nums1D=[4,5,6,0,0,0]
m4=3
nums2D=[1,2,3]
n4=3
merge(nums1D,n4,nums2D,m4)
print(nums1D)
nums1E=[1,3,5,0,0]
m5=3
nums2E=[2,4]
n5=2
merge(nums1E,n5,nums2E,m5)
print(nums1E)

