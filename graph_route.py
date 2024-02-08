'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6 # 경로 확인: sta = 1, end = 6
'''

'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
방향성 그래프 => 유형 그래프 
두 개의 노드에 대해 경로가 있으면 1, 없으면 0 
'''
V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    u, v = list(map(int, input().split()))
    G[u].append(v)      # 유향 그래프
print(G)

def dfs(sta, end):
    visited = [0] * (end + 1)
    st = []
    visited[sta] = 1
    # 정점에서 할 일?
    while True:
        for w in G[sta]:
            if visited[w] == 0:
                st.append(sta)
                sta = w
                visited[sta] = 1
                break
        else:
            if st:
                sta = st.pop()
            else:
                break
        print(visited)
    return
sta, end = list(map(int, input().split()))
dfs(sta, end)











