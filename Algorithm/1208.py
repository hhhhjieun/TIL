# Flatten
import sys
sys.stdin = open('flatten.txt')


# 10번의 test_case
for test_case in range(1, 11):
    dump = int(input())  # dump 최대 횟수
    height_arr = list(map(int, input().split()))  # 총 100개

    # height 의 개수를 셀 수 있는 빈 인덱스 생성
    cnt_height = [0 for _ in range(101)]
    for height in height_arr:
        cnt_height[height] += 1

    # 가장 높은 곳에서 낮은 곳으로 dump
    # cnt 가 있어야지 dump 가능
    start = 1
    end = 100
    cnt_dump = 0  # dump 횟수

    # dump 최대 횟수까지
    while cnt_dump <= dump:
        # start index 에 값이 존재하지 않는다면 다음 index
        # if를 쓸 경우 한번만 확인하게 됨
        while cnt_height[start] == 0:
            start += 1
        while cnt_height[end] == 0:
            end -= 1

        # dump 되면 낮은 곳과 높은 곳의 갯수는 -1,
        cnt_height[start] -= 1
        cnt_height[end] -= 1
        # start + 1 높이의 갯수와 end - 1 높이의 갯수는 +1
        cnt_height[start + 1] += 1
        cnt_height[end - 1] += 1

        # dump 횟수 +1
        cnt_dump += 1

        # 만약 큰 수와 작은 수의 차이가 1 이하이면 더 이상 수행x
        if end - start <= 1:
            break

    print(f'#{test_case} {end - start}')





