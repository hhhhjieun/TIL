# 1. 문자 -> 숫자
# 2. 숫자 정렬
# 3. 숫자 -> 문자

# str_to_number = {"ZRO" : 0}
# number_to_str = {0 : "ZRO"}

def recur_func(n):
    if n == 0:
        return
    print(n, end=' ')
    recur_func(n-1)
    print(n, end=' ')


recur_func(5)



