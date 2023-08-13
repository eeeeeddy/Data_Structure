# Graph

- **그래프**
    - Vertex(노드)와 Edge(간선)로 이루어진 자료구조 → **G = (V, E)**
        - 연결되어 있는 객체 간의 관계를 표현할 수 있는 자료구조
    - Edge Type
        - Directed Edge(유향 그래프)
            - 노드 (u, v)의 순서쌍으로 이루어짐
            - u : head, v : tail
            - 방향성이 있음
            - Ex : 항공편
            - Directed Edge로 생성된 그래프를 **Directed Graph**라고 함 → **E(u, v) = E(v, u)**
        - Undirected Edge(무향 그래프)
            - 노드 (u, v)의 쌍으로 이루어지며 순서의 구분이 없음
            - Ex : 인터넷 네트워크
            - Undirected Edge로 생성된 그래프를 **Undirected Graph**라고 함 → **E(u, v) != E(v, u)**

- **용어**
    - 정점(Vertex) : 고정된 위치, 점을 의미, 노드라고도 함
    - 간선(Edge) : 위치간의 관계. 즉 노드를 연결하는 선
    - 인접 정점(Adjacent Vertex) : 간선에 의해 직접 연결된 정점
    - 정점의 차수(Degree) : 무향 그래프에서 하나의 정점에 인접한 간선의 수 ( 정점 X의 차수는 5 )
    - 진입 차수(In-Degree) : 유향 그래프에서 외부에서 들어오는 간선의 수
    - 진출 차수(Out-Degree) : 유향 그래프에서 외부로 향하는 간선의 수
    - 경로(Path) : 정점 u에서부터 정점 v까지 연결되는 정점과 간선의 배열
    - 경로 길이(Path Length) : 정점 u에서부터 정점 v까지 연결되는 경로를 구성하는 데 사용된 간선의 수
    - 단순 경로(Simple Path) : 경로 중에서 반복되는 정점과 간선이 없는 경우
    - 순환(Cycle) : 경로의 시작 정점과 종료 정점이 동일한 경우
    - 단순 순환(Simple Cycle) : 순환 중에서 반복되는 정점과 간선이 없는 경우
    - 자체 간선(Self Loop) : 간선 j

        ![1](https://github.com/eeeeeddy/Data_Structure/assets/71869717/9de5bfc7-947d-4909-8f1b-a69650af4428)

        ![2](https://github.com/eeeeeddy/Data_Structure/assets/71869717/bafca7e3-93e5-40e3-8c52-738873ab223f)

        ![3](https://github.com/eeeeeddy/Data_Structure/assets/71869717/48237033-a2f6-4856-a593-563f1f63a03d)

- **특징**
    - 모든 Degree의 합은 간선의 수의 **2배**
    - 그래프는 **네트워크 모델**
    - 2개 이상의 경로가 가능하다
        - 즉, 노드들 사이에 무향/유향에서 양방향 경로를 가질 수 있다.
    - self-loop뿐 아니라 loop와 circuit 모두 가능하다.
    - 루트노드, 부모-자식관계라는 개념이 없다.

- **Graph vs Tree**
    
    
    |  | Graph | Tree |
    | --- | --- | --- |
    | 정의 | 정점과 그 정점을 연결하는 간선의 집합 | 그래프의 한 종류 <br> DAG(Directed Acyclic Graph, 방향성이 있는 비순환 그래프)의 한 종류 |
    | 방향성 | 무향 그래프, 유향 그래프 | 방향 그래프(Root → Leaf) |
    | 사이클 | - 가능 <br> - 자체 간선(Self-Loop)도 가능 <br> - 순환 그래프, 비순환 그래프 모두 존재 | - 불가능 <br> - 자체 간선 불가능 <br> - 비순환 그래프 |
    | 루트 노드 | X | - 한 개의 루트 노드만이 존재 <br> - 모든 자식 노드는 한 개의 부모 노드만을 가짐 |
    | 부모-자식 관계 | X | O |
    | 모델 | 네트워크 모델 | 계층 모델 |
    | 순회 | DFS, BFS | DFS, BFS 안의 Preorder, Inorder, Postorder |
    | 간선의 수 | 그래프에 따라 간선의 수가 다름 <br> 간선이 없을 수도 있음 | 노드가 N개인 트리는 항상 N-1개의 간선을 가짐 |
    | 경로 | - | 임의의 두 노드간의 경로는 유일 |

- **그래프의 종류**
    - 가중치 그래프(Weighted Graph)
        - 간선에 가중치가 할당된 그래프
    - 연결 그래프(Connected Graph)
        - 무향 그래프에 있는 모든 정점 쌍에 대해서 항상 경로가 존재하는 경우
        - 트리는 순환이 없는 연결 그래프
    - 비연결 그래프(Disconnected Graph)
        - 무향 그래프에서 특정 정점 쌍 사이에 경로가 존재하지 않는 경우
    - 비순환 그래프(Acyclic Graph)
        - 순환이 없는 그래프
    - 완전 그래프(Complete Graph)
        - 그래프에 속해있는 모든 정점이 서로 연결된 그래프
        - 무향 완전 그래프의 간선 수 : 정점의 갯수가 n일 때, **n*(n-1) / 2**
<br><br>
- **그래프의 구현 방법**
    - 인접 리스트로 구현 (Adjacency List) → **일반적인 구현 방법**
        
        ![4](https://github.com/eeeeeddy/Data_Structure/assets/71869717/60f21abf-6396-4b5c-92f3-b384461e39fe)
        ![5](https://github.com/eeeeeddy/Data_Structure/assets/71869717/11c8b16f-f9ac-4bbb-ae3b-09700ba6862c)
        
        - 모든 정점을 인접 리스트에 저장 (즉, 각각의 정점에 인접한 정점을 리스트로 표현)
            - 배열(또는 해시 테이블)과 배열의 각 인덱스마다 존재하는 또 다른 리스트(배열, 연결 리스트로 구현)
        - 정점의 값만 알면 이 값을 배열의 인덱스로하여 각 정점의 리스트에 쉽게 접근할 수 있다.
        - 무향 그래프에서 **E(u, v)**은 2번 저장됨
        - 그래프에선 특정 노드에서 다른 모든 노드로 접근이 불가능함 → Graph 클래스 필요
<br><br>
    - 인접 행렬로 구현 (Adjacency Matrix)
        
        ![6](https://github.com/eeeeeddy/Data_Structure/assets/71869717/92b1515e-e22e-4156-ac75-c5003398576c)
        ![7](https://github.com/eeeeeddy/Data_Structure/assets/71869717/35c2a7dc-f6d0-4dbc-bab0-f13db56f2c42)
        
        - N x N Boolean Matrix로써 matrix[i][j]가 true라면 i → j로의 간선이 존재함을 의미 (N : 정점의 수)
        - 0과 1을 사용해서도 표현이 가능
            
            ```
            if( E(i, j)가 그래프에 존재):
              matrix[i][j] = 1
            else:
              matrix[i][j] = 0
            ```
            
        - 정점의 갯수에 따라 행렬의 크기가 정해지기 때문에 간선의 수와는 무관하게 항상 N^2개의 메모리 공간이 필요
        - 무향 그래프를 표현하면 항상 대칭 행렬임

- **그래프 코드**
    - Easy version
        
        ```python
        #무방향 그래프
        graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]}
        
        #방향 그래프
        graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}
        ```
        
    - 인접 리스트를 활용한 방향 그래프 구현
        
        ```python
        # 그래프 객체를 나타내는 클래스
        class Graph:
            # 생성자
            def __init__(self, edges, n):
                # 인접 리스트에 대한 메모리 할당
                self.adjList = [[] for _ in range(n)]
        
                #는 방향 그래프에 간선을 추가합니다.
                for (src, dest) in edges:
                    #는 인접 리스트의 노드를 src에서 dest로 할당합니다.
                    self.adjList[src].append(dest)
        
        # 그래프의 인접 리스트 표현을 인쇄하는 기능
        def printGraph(graph):
            for src in range(len(graph.adjList)):
                # 현재 정점과 모든 인접 정점을 인쇄합니다.
                for dest in graph.adjList[src]:
                    print(f'({src} —> {dest}) ', end='')
                print()
        
        if __name__ == '__main__':
        
            # 입력: 유향 그래프의 간선
            edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
        
            # 꼭짓점 수(0에서 5까지 레이블 지정)
            n = 6
        
            #는 주어진 간선 리스트에서 그래프를 구성합니다.
            graph = Graph(edges, n)
        
            # 그래프의 인접 리스트 인쇄
            printGraph(graph)
        
        >>>>>>>>>>>>>>>>>>>>>>>>
        (0 —> 1)
        (1 —> 2)
        (2 —> 0) (2 —> 1)
        (3 —> 2)
        (4 —> 5)
        (5 —> 4)
        ```
        
    - 인접 리스트를 활용한 가중치 방향 그래프 구현
        
        ```python
        # 그래프 객체를 나타내는 클래스
        class Graph:
            # 그래프를 구성하는 생성자
            def __init__(self, edges, n):
        
                # 인접 리스트을 나타내는 목록 목록
                self.adjList = [None] * n
        
                # 인접 리스트에 대한 메모리 할당
                for i in range(n):
                    self.adjList[i] = []
        
                #는 방향 그래프에 간선을 추가합니다.
                for (src, dest, weight) in edges:
                    #는 인접 리스트의 노드를 src에서 dest로 할당합니다.
                    self.adjList[src].append((dest, weight))
        
        # 그래프의 인접 리스트 표현을 인쇄하는 기능
        def printGraph(graph):
            for src in range(len(graph.adjList)):
                # 현재 정점과 모든 인접 정점을 인쇄합니다.
                for (dest, weight) in graph.adjList[src]:
                    print(f'({src} —> {dest}, {weight}) ', end='')
                print()
        
        if __name__ == '__main__':
        
            # 입력: 가중 이중 그래프의 에지(위 다이어그램에 따름)
            # Edge (x, y, w)는 가중치가 `w`인 `x`에서 `y`까지의 에지를 나타냅니다.
            edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
                    (4, 5, 1), (5, 4, 3)]
        
            # 꼭짓점 수(0에서 5까지 레이블 지정)
            n = 6
        
            #는 주어진 간선 리스트에서 그래프를 구성합니다.
            graph = Graph(edges, n)
        
            # 그래프의 인접 리스트 인쇄
            printGraph(graph)
        
        >>>>>>>>>>>>>>>>>>>>>>>>
        (0 —> 1, 6)
        (1 —> 2, 7)
        (2 —> 0, 5) (2 —> 1, 4)
        (3 —> 2, 10)
        (4 —> 5, 1)
        (5 —> 4, 3)
        ```
        
    - 인접 행렬을 활용한 무향 그래프 구현
        
        ```python
        class Adjacency_Matrix:
            def __init__(self, vertices):
                self.vertices = vertices
                self.graph = [[0 for j in range(self.vertices)] for i in range(self.vertices)]
        
            def addEdge(self, v1, v2):
                self.graph[v1][v2] = 1
                self.graph[v2][v1] = 1
        
            def printGraph(self):
                for row in range(self.vertices):
                    for column in range(self.vertices):
                        print(self.graph[row][column], end=' ')
                    print('')
        ```
        
    - 인접 행렬을 활용한 유향 그래프 구현
        
        ```python
        class Adjacency_Matrix:
            def __init__(self, vertices):
                self.vertices = vertices
                self.graph = [[0 for j in range(self.vertices)] for i in range(self.vertices)]
        
            def addEdge(self, v1, v2):
                self.graph[v1][v2] = 1
        
            def printGraph(self):
                for row in range(self.vertices):
                    for column in range(self.vertices):
                        print(self.graph[row][column], end=' ')
                    print('')
        ```
        
---

- 참고자료
    - [https://sennieworld.tistory.com/36](https://sennieworld.tistory.com/36)
    - [https://velog.io/@jjaa9292/Python%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-6.%EA%B7%B8%EB%9E%98%ED%94%84](https://velog.io/@jjaa9292/Python%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-6.%EA%B7%B8%EB%9E%98%ED%94%84)
    - [https://codermun-log.tistory.com/286](https://codermun-log.tistory.com/286)
    - [https://www.techiedelight.com/ko/graph-implementation-python/](https://www.techiedelight.com/ko/graph-implementation-python/)