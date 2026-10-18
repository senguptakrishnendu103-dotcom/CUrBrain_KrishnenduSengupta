def divisiblePrefix(arr,k):
    k=abs(k)
    if k==0:
        return False
    prefix_sum=0
    for i in arr:
        prefix_sum+=i
        if prefix_sum%k==0:
            return True
    return False
print(divisiblePrefix([4, 2, 9], 3))
print(divisiblePrefix([1, 2, 4], 5))
print(divisiblePrefix([5], 5))
print(divisiblePrefix([0, 1], 7))
print(divisiblePrefix([-2, 2, 1], 3))