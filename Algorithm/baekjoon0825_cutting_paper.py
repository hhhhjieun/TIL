# 종이 자르기
'''
가로 점선(행 번호) : 0
세로 점선(열 번호) : 1
'''
import sys

width, height = map(int, sys.stdin.readline())
N = int(sys.stdin.readline())
paper = [0 * (width + 1) for _ in range(height + 1)]


for i in range(N):
    cut = list(map(int, sys.stdin.readline().split()))




