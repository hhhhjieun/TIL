# 퀵 정렬
T = int(input())

def quick_sort(arr):
   if len(arr) <= 1:
       return arr

   pivot = arr[0]
   tail = arr[1:]

   left_side, right_side = [], []

   for num in tail:
       if num <= pivot:
           left_side.append(num)
       else:
           right_side.append(num)

   return quick_sort(left_side) + [pivot] + quick_sort(right_side)


for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = quick_sort(arr)
    ans = result[N//2]

    print(f'#{test_case} {ans}')