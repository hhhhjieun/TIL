# views
import sys
sys.stdin = open('input.txt')


T = 10

for test_case in range(1, T + 1):
    N = int(input())   # 건물의 개수
    arr = list(map(int, input().split()))   # N개의 건물의 높이

    result = 0

    for i in range(2, N-2):  # 맨 왼쪽과 맨 오른쪽 두칸 x
        # 현재 조사대상의 높이 : 최대 조망권
        tmp = arr[i]

        for j in range(i-2, i+3):
            # 나랑 나를 비교할 필요x
            if i == j:
                continue
            # 조사 대상이 양 옆보다 크고,
            # 그 둘의 차이가 최대 조망권보다 작으면,
            if arr[i] > arr[j] and tmp > arr[i] - arr[j]:
                tmp = arr[i] - arr[j]  # 최대 조망권 변경

            # 만약 조사 댕의 양옆이 나와 크기가 같은 경우가 한번이라도 있으면,
            # 더이상 조사할 필요x
            elif arr[i] <= arr[j]:
                tmp = 0
                break  # 바로 상위의 순회만 종료

        # break 문으로 종료되지 않았다면.(더 이상 조사할 필요가 없는 경우가 없었다면)
        # 정상적으로 모든 조사가 끝났다
        # i 번째 위치 건물의 조망권 크기 더하기
        result += tmp

    print(f'#{test_case} {result}')

