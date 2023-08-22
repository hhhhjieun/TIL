# 이진 힙
# 최소힙

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # node 개수
    arr = list(map(int, input().split()))

    min_heap = [0] * (N+1)  # 완전 이진 트리
    last = 0

    for i in arr:
        # arr 순서대로 heap 저장
        last += 1
        min_heap[last] = i

        # 최소힙 확인
        c = last  # 자식

        while (c//2) > 0 and min_heap[c//2] > min_heap[c]:  # 부모가 있고, 부모가 더 크면
            min_heap[c//2], min_heap[c] = min_heap[c], min_heap[c//2]  # 부모 <-> 자식
            c = c // 2  # 자식 변경
            p = c // 2  # 부모 변경

    # 마지막 노드(N)의 조상 노드 합
    total = 0
    P = N // 2  # 부모 노드는 자식 노드 // 2
    while P > 0:  # 부모가 없을 때 까지
        total += min_heap[P]
        P //= 2

    print(f'#{test_case} {total}')

'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    tree = [0] * (N+1)
    
    # 입력받은 완전 이진트리를 저장, 1번 인덱스부터 사용
    # 0번 인덱스는 사용하지 않음
    
    for i in range(1, N + 1):
        tree[i] = arr[i-1]
        
        # i가 1보다 크다면, 부모 노드가 있다.
        # 부모 노드와 비교후, 이진 최소힙 구성 조건에 맞게 swap 할지 결정
        while i >= 2:
            parent = i // 2
            if tree[i] <= tree[parent]:  # 
                tree[i], tree[parent] = tree[parent], tree[i]
            i = N // 2  # 부모 노드의 위치 변경
            
    
    
'''





