# Graph Traversal (DFS / BFS)

- **그래프 순회 (Graph Traversal)**
    - 임의의 한 정점에서 시작하여 모든 정점들을 한 번씩 방문하는 작업
<br><br>
- **깊이 우선 탐색 (Depth First Search)**
    - 임의의 한 노드에 연결된 노드 중 하나를 골라 순회를 더이상 진행할 수 없을 때까지(인접 노드 중 한번도 방문하지 않은 노드가 없을 때까지) 탐색한다.
    그 후 더이상 진행이 불가능하면, 진행이 가능한 노드까지 되돌아와 그 다음 탐색을 진행한다.
    
      <div style="background-color : white">
        <img src="https://github.com/eeeeeddy/Data_Structure/assets/71869717/189d2724-8801-491f-bfa6-a4272f1b30eb">
      </div>
      <br>
- 구현 방법
    1. 임의의 시작 노드를 방문하고 방문했다고 표시한다.
    2. 시작 노드에 인접한 모든 노드 중 방문하지 않은 노드가 있는지 확인한다.
    3. 인접 노드 중 방문하지 않은 노드가 있다면 그 노드를 현재 노드로 정하고 [과정 a]로 돌아간다.
    4. 더이상 방문할 노드가 없다면 종료
<br><br>
- DFS Pseudo Code : **Stack & Recursion** 사용
    
    ```
    def DFS_Traverse(G):
      input graph G = (V, E)
    
      for all u ∈ V:
        mark u as UNVISITED
      for all v ∈ V:
        if v is marked as UNVISITED
        DFS(G, v)
    ```
    
    ```
    def DFS(G, v):
      input graph G = (V, E) and a start vertex v ∈ V
    
      mark v as VISITED
      for all w ∈ {neighbor of v}:
        if w is marked as UNVISITED:
          DFS(G, w)
    ```
    

- 구현 코드
    
    ```python
    # 그래프 구현
    from queue import Queue
    
    class Graph:
        def __init__(self, vertex_num):
            self.adj_list = [[] for _ in range(vertex_num)]
            self.visited = [False for _ in range(vertex_num)]
    
        def add_edge(self, u, v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    
        def init_visited(self):
            for i in range(len(self.visited)):
                self.visited[i] = False
    ```
    
    ```python
    # 재귀 함수 이용
    def __dfs_recursion(self, v):           # 매개변수 v를 먼저 방문 후 v와 인접한 adj_v의 리스트에 있는 모든 정점을 방문. 방문하지 않은 정점을 만날 때는 재귀함수 호출
            print(v, end='=')
            self.visited[v] = True
    
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    self.__dfs_recursion(u)
    
        def dfs(self, v):                    # 재귀 함수를 수행하기 전 방문 리스트 초기화
            self.init_visited()
            self.__dfs_recursion(v)
    ```
    
    ```python
    # 스택과 반복문 이용
    def iter_dfs(self, v):
            s = Stack()
            self.init_visited()
    
            s.push(v)                           # 최초 방문한 정점을 stack에 쌓음
            self.visited[v] = True
    
            print(v, end='=')
    
            is_visited = False                  # 아직 방문하지 않은 정점의 방문 여부 체크
    
            while not s.empty():
                is_visited=False
                v = s.peak()                    # 스택의 메서드로 변형없이 맨 위의 값을 출력
    
                adj_v = self.adj_list[v]
                for u in adj_v:
                    if not self.visited[u]:
                        s.push(u)
                        self.visited[u] = True
                        is_visited = True       # 인접 정점들에 대해 순회하면서 방문하지 않은 정점을 만난 경우 True로 변경 후,
                        break                   # 방문하지 않았던 정점들에 대해 for문을 빠져나가 while 루프를 다시 수행
            if not is_visited:
                s.pop()
    ```
    

- 시간 복잡도
    - 인접 리스트 : O(V+E)
    - 인접 행렬 : O(V^2)
<br><br>
- **너비 우선 탐색 (Breadth First Search)**
    - 임의의 한 노드에 연결된 노드를 우선적으로 탐색하는 방법 (같은 레벨을 먼저 탐색 후 다음 레벨 탐색)
    
      <div style="background-color : white">
        <img src="https://github.com/eeeeeddy/Data_Structure/assets/71869717/0b5d26f8-6021-4cea-aac4-1930454a9944">
      </div>
      <br>
- 구현 방법
    1. 임의의 시작 노드를 정해 큐에 넣는다.
    2. Dequeue 연산을 통해 큐에서 노드를 가져와 현재 노드로 정한다.
    3. 현재 노드의 인접 노드 목록을 순회하면서 방문하지 않은 노드가 있는지 확인한다.
    4. 방문하지 않은 노드가 있다면 그 노드를 큐에 넣고 방문한다.
    5. 큐가 비어있게 될 때까지 **[과정 b] ~ [과정 d]**를 반복
<br><br>
- BFS Pseudo Code : **Queue** 사용
    
    ```
    def BFS_Traverse(G):
      input graph G = (V, E)
    
      for all u ∈ V:
        mark u as UNVISITED
      for all v ∈ V:
        if v is marked as UNVISITED:
          BFS(G, v)
    ```
    
    ```
    def BFS(G, s):
      L_0 ← new empth Queue
      L_0.append(s)
      mark s as VISITED
      i ← 0
      while L_i is not empty:
        L_i+1 ← new empty Queue
        for all v ∈ L_i.elements():
          for all w ∈ {neighbors of v}:
            if w is marked as UNVISITED:
              mark w as VISITED
              L_i+1.append(w)
        i ← i + 1
    ```
    

- 구현 코드
    
    ```python
    # 그래프 구현
    from queue import Queue
    
    class Graph:
        def __init__(self, vertex_num):
            self.adj_list = [[] for _ in range(vertex_num)]
            self.visited = [False for _ in range(vertex_num)]
    
        def add_edge(self, u, v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    
        def init_visited(self):
            for i in range(len(self.visited)):
                self.visited[i] = False
    ```
    
    ```python
    def bfs(self, v):
            q = Queue()                     # Queue 생성
    
            self.init_visited()             # 방문 체크리스트 초기화
    
            q.put(v)                        # 첫 번째 정점을 큐에 넣음
            self.visited[v] = True          # 첫 번째 정점 방문 완료
    
            while not q.empty():            # Queue가 비어있을 때까지 while문 수행하면서 모든 정점 방문
                v = q.get()                 # 이미 방문한 정점 dequeue
                                            # get()을 통해 Queue의 front 값을 pop하면서 그 값을 다음 정점으로 선정
                print(v, end='=')
                adj_v = self.adj_list[v]    # 이미 방문한 정점의 인접 정점 리스트
    
                for u in adj_v:             # 반복문을 수행하면서 방문하지 않은 정점을 Queue에 넣고
                    if not self.visited[u]: # 최초 v의 인접 정점의 방문 여부를 True로 변경
                        q.put(u)
                        self.visited[u] = True
    ```
    

- 시간 복잡도
    - 인접 리스트 : O(V+E)
    - 인접 행렬 : O(V^2)

---

- 또 다른 구현 코드
    
    ```python
    class myGraph:
      def __init__(self):
        self.graph = {}
    
      def addInfo(self, startV, endVs):
        self.graph[startV] = endVs
    
      def addEdge(self, startV, endV):
        self.graph[startV].append(endV)
    
      def addVertex(self, V):
        self.graph[V] = []
    
      def bfs(self, startV):
        q = [startV]
        visited = [startV]
        while q:
          # 자료양이 커지면 deque.popleft()를 쓰는게 시간이 빠르다.
          nowV = q.pop(0)
          for nextV in self.graph[nowV]:
            if nextV not in visited:
              q.append(nextV)
              visited.append(nextV)
        return visited
    
      def dfs(self, startV):
        s = [startV]
        visited = []
        while s:
          nowV = s.pop()
          if nowV not in visited:
            visited.append(nowV)
            s.extend(self.graph[nowV][::-1])
        return visited
    
      def dfs_recursive(self, startV, visited=[]):
        visited.append(startV)
    
        for nextV in self.graph[startV]:
          if nextV not in visited:
            self.dfs_recursive(nextV, visited)
    
        return visited
    
    g = myGraph()
    g.addInfo( 'A', ['B',  'E',  'I'])
    g.addInfo( 'B', ['A',  'C'])
    g.addInfo( 'C', ['B',  'D'])
    g.addInfo( 'D', ['C'])
    g.addInfo( 'E', ['A',  'F',  'H'])
    g.addInfo( 'F', ['E',  'G'])
    g.addInfo( 'G', ['F'])
    g.addInfo( 'H', ['E'])
    g.addInfo( 'I', ['A',  'J'])
    g.addInfo( 'J', ['I'])
    
    print(g.bfs('A'))
    print(g.dfs('A'))
    print(g.dfs_recursive('A'))
    
    # ['A', 'B', 'E', 'I', 'C', 'F', 'H', 'J', 'D', 'G']
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    ```
    

---

- 참고자료
    - [https://velog.io/@jjaa9292/Python%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-6.%EA%B7%B8%EB%9E%98%ED%94%84](https://velog.io/@jjaa9292/Python%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-6.%EA%B7%B8%EB%9E%98%ED%94%84)
    - [https://gamedevlog.tistory.com/32](https://gamedevlog.tistory.com/32)
    - [https://gmlwjd9405.github.io/2018/08/13/data-structure-graph.html](https://gmlwjd9405.github.io/2018/08/13/data-structure-graph.html)
    - [https://wikidocs.net/196183](https://wikidocs.net/196183)
    - [https://wikidocs.net/196284](https://wikidocs.net/196284)
    - [https://rhdtka21.tistory.com/140](https://rhdtka21.tistory.com/140)