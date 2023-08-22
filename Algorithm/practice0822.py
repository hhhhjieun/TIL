'''

# 힙
def deq():
    global last
    tmp = heap[1]  # 루트 백업
    heap[1] = heap[last]  # 삭제할 노드의 키를 루트에 복사
    last -= 1  # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식(비교할 자식노드 번호)
    while c <= last:  # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1  # 비교 대상이 오른쪽 자식노드
            if heap[p] < heap[c]:  # 자식이 더 크면 최대힙 규칙에 어근나므로
                heap[p], heap[c] = heap[c], heap[p]
                p = c  # 자식을 새로운 부모로
                c = p * 2  # 왼쪽 자식 번호를 계산
            else:  # 부모가 더 크면
                break  # 비교 중단

    return tmp


heap = [0] * 100
last = 0

'''

'''
N = int(input())
data = [input().split() for _ in range(N)]

# 자식 노드가 없을때, 인덱스를 맞추자
data.insert(0, [0, 0, 0, 0])

for d in data:
    while len(d) != 4:
        d.append('0')
        
        
# 데이터 인풋 -> 우리가 가공해서 처리해야할 데이터를 받는다
# 우리가 활용하기 편한 자료구조를 택하고, 전처리를 한다.

# IM :
# 주어진 데이터를 적절한 자료구조에 담아
# 핵심 : 2차원 배열

'''

# 힙 -> 트리의 한 종류
# 최댓값, 최솟값 -> 우선순위 큐

# 트리에서 삽입과 삭제 이루어진다.
# 루트 노드가 가장 높은 우선순위를 갖는다.
# node 삭제할 때, 반드시 루트 노드를 삭제한다.
