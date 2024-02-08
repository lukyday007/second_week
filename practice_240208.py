# # stack 연습
# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
#
# # 마지막 정점 번호 V, 간선 수 E
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# # 인접리스트
# adjl = [[] for _ in range(V+1)] # adgl[i] 행 i에 인접인 정점 번호
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2 + 1]
#     adjl[n1].append(n2)
#     adjl[n2].append(n1) # 방향이 없는 경우 ( 조건 잘 파악 )
#
# def dfs(i, V):     # 시작 i, 마지막 V
#     # visited, stack 생성 및 초기화, 마지막 정점 번호 필요
#     visited = [0] * (V + 1)
#     st = []
#     visited[i] = 1      # 시작점 방문
#     print(i)            # 정점에서 할 일
#     while True:     # 탐색
#         # 현재 방문한 정점에서 인접하고 방문 안 한 정점 W가 잇으면
#         for w in adjl[i]:
#             if visited[w] == 0:
#                 st.append(i)    # push(i), i를 지나서
#                 i = w           # w 에 방문
#                 visited[i] = 1  # 방문해서 할 일
#                 print(i)
#                 break
#         else:                   # i에 남은 인접정점이 없으면
#             # 스택이 비어있지 않으면 ( 지나온 정점이 남아 있으면 )
#             if st:  # top != -1
#                 i = st.pop()
#             else:   # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
#                 break   # while True
#     return  # 끝
# dfs(1, V)   # 입력방식이 정렬되지 않으면 순서가 다르게 나올 수 있다

'''
Graph는 정점(vertex)들과 간선(edge)들의 집합
숫자 데이터로 바꾸어서 처리
노드와 그들 사이의 관계를 표현
유향/ 무향
관계를 따라가면 관계에 따른 정보 획득 가능
인접하다 = 간선이 있다
1 - > 2 : 2는 1의 인접정점이다(O) , 1는 2의 인접정점이다(X)
따라서 유향, 무향 그래프는 다르게 저장되어야 함
그래프를 저장하는 방법: 간선들의 정보 저장, 각 정점들의 인접 정점들을 저장
간선 하나 표현 - 두 개의 정점 정보 필요 (숫자화: 양의 정수)
그래프를 그릴 때 간선 정보들이 주어짐
정점수, 간선수 = 5, 5
1 - 정점수(까지의 번호를 사용)
1 2 / 1 3 / 2 4 / 2 5 / 3 5 -> 저장
[ 2가지 저장행렬 ]
1. 인접 행렬
2. 인접 리스트  ( 파이썬의 장점 : 리스트의 리스트 )
'''

# 인접 리스트로 저장하기
''' 유향, 무향 체크 
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 빈 리스트를 정점의 개수만큼 만들기
G = [[] for _ in range(V + 1)]  # 0을 안쓰니까, 정점 번호가 1부터 시작 -> V + 1
for i in range(0, E*2, 2): # e * 2 = 16
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)  # 무향 그래프라서 추가 가능

for i in range(1, V+1):
    print(i, "-->", G[i])















