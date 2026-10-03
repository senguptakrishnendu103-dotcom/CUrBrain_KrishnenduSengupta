def s_p_s(n):
    sum_digit=0
    pro_digit=1

    while n>0:
        digit=n%10

        sum_digit +=digit
        pro_digit *=digit

        n=n//10

    return pro_digit-sum_digit

print(s_p_s(234))
print(s_p_s(123))
print(s_p_s(5))
print(s_p_s(100))
print(s_p_s(999))