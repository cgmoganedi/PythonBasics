def fact_two():
    a = 2
    ans = a
    while a > 1:
        ans *= (a-1)
        a -=  1
    return ans
