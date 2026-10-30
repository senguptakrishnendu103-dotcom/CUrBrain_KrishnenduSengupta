def second_highest(scores):
    highest=-1
    second=-1

    for num in scores:
        if num > highest:
            second=highest
            highest=num
        elif  num<highest and num>second:
            second=num
    return second

print(second_highest([50,40,50,30] ))
print(second_highest([100,100,100] ))
print(second_highest([] ))
print(second_highest([10,20,30,40] ))
print(second_highest([5,5,4,4,3] ))