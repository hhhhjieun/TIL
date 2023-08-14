# BruteForce
'''
BruteForce(고지식한 패턴 검색)
: 문자열의 처음부터 끝까지 순차적으로 순회하면서 패턴 내의
문자들을 일일이 비교하는 방식
'''
p = "is"
t = "This is a book~!"
M = len(p)
N = len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

    if j == M:  # 탐색 성공
        return i - M
    else:
        return -1


# push
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20
print(stack)

# pop
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]

print(pop())

if top > -1:
    top -= 1
    print(stack[top+1])

# memoization
'''
: 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여
전체적인 실행속도를 빠르게 하는 기술
'''

def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

# dp
'''
동적 계획(dynamic programming)
: 입력의 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여
보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 
문제를 해결하는 알고리즘
'''

def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

# dfs
'''
: 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 
더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로
되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을
방문하는 순회방법
'''

def dfs(n,V,adj_m):
    stack = []  # 정점
    # result = []  # 결과를 저장할 리스트
    visited = [False] * (V+1)  # 방문 정점
    visited[n] = True  # 시작 정점
    # result.append(n)

    while True:
        for w in range(1, V + 1):
            if adj_m[n][w] == 1 and visited[w] is False:
                stack.append(n)
                n = w
                visited[n] = True
                # result.append(n)
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    return

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 노드, 간선 개수

    adj_m = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1

    S, G = map(int, input().split())  # 출발, 도착 노드

    result = [dfs(S, V, adj_m)]


