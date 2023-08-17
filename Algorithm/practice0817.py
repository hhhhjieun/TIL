'''
# cQueue
def enq(data):
    global rear
    global front
    if (rear+1) % cQsize == front:  # front 를 밀면서 저장
        front = (front+1) % cQsize
    rear = (rear+1) % cQsize
    cQ[rear] = data


def deq():
    global front
    front = (front+1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)

print(deq())  # 3
print(deq())  # 4
print(deq())  # 5
print(deq())  # 2

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q.popleft())  # 1
print(q.popleft())  # 2
print(q.popleft())  # 3
'''

n = 5  # queue 의 크기

rear = front = -1

my_q = [None] * 5  # queue 생성

# addQ
my_q[rear] = 'A'
rear += 1

# deQ
my_q[front] = None
front += 1

class LinearQueue:
    def __init__(self, size):
        self.size = size  # q 의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = -1

    # 공백 상태
    def is_empty(self):
        return self.front == -1  # front 가 -1 이면 q가 공백상태

    # 포화 상태
    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if self.is_full():  # 포화 상태 체크
            print("현재 큐가 포화 상태 입니다.")
            return
        elif self.is_empty():  # 선형큐의 문제점 해결 : 앞에 비어있다면
            self.front = self.rear = 0  # item 이 하나라면 front = rear : 초기화

        self.rear = self.rear + 1  # rear 값을 다음으로 이동
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("현재 큐가 비어있습니다.")
            return None

        item = self.queue[self.front]  # front 아이템 반환
        # deq 아이템 하나 남은 경우, 큐 초기화
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = self.front + 1

        return item


queue = LinearQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # 큐가 가득 참 에러 발생

print(queue.queue)

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    '''
    큐의 시작과 끝이 연결되어있다.
    큐의 포화상태를 판별하기 위해서 rear 의 다음요소 % self.size
    큐가 가득 찼다면, (4 + 1) % 5 = 0
    '''

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def enq(self, item):
        if self.is_full():
            raise Exception("Queue is Full!!!")

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def deq(self):
        if self.is_empty():
            raise Exception("Queue is Empty!!!")

        self.front = (self.front + 1) % self.size
        return self.queue[self.front]
