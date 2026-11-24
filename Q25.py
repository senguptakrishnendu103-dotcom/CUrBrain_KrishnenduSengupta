def closest_pair(temps,target):
    left=0
    right=len(temps)-1
    min_diff=float('inf')
    best_pair=()
    while left<right:
        current_sum=temps[left]+temps[right]
        diff=abs(current_sum-target)
        if diff<min_diff:
            min_diff=diff
            best_pair=(temps[left],temps[right])
        if current_sum<target:
            left+=1
        elif current_sum>target:
            right-=1
        else:
            break
    return best_pair
temps1=[10,22,28,29,30,40]
target1=54
print(closest_pair(temps1,target1))
temps2=[1,3,5,9]
target2=8
print(closest_pair(temps2,target2))
temps3=[1,2]
target3=100
print(closest_pair(temps3,target3))
temps4=[-4,-1,2,6]
target4=3 
print(closest_pair(temps4,target4))
temps5=[10,20,30]
target5=5
print(closest_pair(temps5,target5))   