def filter_sales(sales,threshold):
    result=[]

    for num in sales:
        if num>=threshold:
            result.append(num)
    return result

sales1=[150,80,200,90,300]
threshold1=100 
sales2=[100,50,100]
threshold2=100 
sales3=[]
threshold3=50 
sales4=[10,20,30]
threshold4=40 
sales5=[75,75,75]
threshold5=75

print(filter_sales(sales1,threshold1))
print(filter_sales(sales2,threshold2))
print(filter_sales(sales3,threshold3))
print(filter_sales(sales4,threshold4))
print(filter_sales(sales5,threshold5))