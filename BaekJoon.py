import sys
'''첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.'''
#print("테스트 케이스 수:")
T = int(sys.stdin.readline())
for i in range(0,T):
    #print("출력:")
    A, B = map(int,sys.stdin.readline().split())
    sum = A + B
    print(sum)

