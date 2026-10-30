def find_mode(sales):
    fre={}

    for num in sales:
        if num in fre:
            fre[num]+=1
        else:
            fre[num]=1

    max_fre=0
    result=0

    for num in fre:
        if fre[num]>max_fre:
            max_fre=fre[num]
            result=num
        elif fre[num]==max_fre and num<result:
            result=num
    return result
sales1 =[101,103,101,102,103,105,101,103] 
sales2 =[5,5,5,2,2,2,2]
sales3=[99]
sales4=[-2,-2,3,3,0]
sales5=[4,1,4,1,7] 
print(find_mode(sales1))
print(find_mode(sales2))
print(find_mode(sales3))
print(find_mode(sales4))
print(find_mode(sales5))

