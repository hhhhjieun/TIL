# Ladder1
'''
1. 100번째 행에서 2를 찾는다
2. 양 옆의 숫자가 0이면 앞으로 이동(행 -1)
3. 양 옆의 숫자가 1이면 1인 방향으로 이동
4. 1번째 행 도착하면 그 값을 3으로 변경
5. 그 행에서 3번의 인덱스 값 + 1 출력
'''
import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 시작값 초기화
    start_idx = 0

    # 100번째 행(99번) 에서 2의 값이 있는 열을 찾는다
    for j in range(100):
        if arr[99][j] == 2:
            start_idx = j   # 시작 열

    for c in range(98, 0, -1):  # 일단 앞으로 한번 가고 시작
        # 양 옆 확인
        if arr[c][start_idx - 1] == 1 and start_idx != 0:
            while arr[c][start_idx - 1] == 1:
                if start_idx == 0:
                    break
                else:
                    start_idx -= 1
        # and 순서 중요
        elif start_idx != 99 and arr[c][start_idx + 1] == 1:
            while arr[c][start_idx + 1] == 1:
                if start_idx == 98:
                    start_idx += 1
                    break
                else:
                    start_idx += 1

    print(f'#{test_case} {start_idx}')














