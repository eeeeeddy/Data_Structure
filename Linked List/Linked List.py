class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.curr = None
    
    def __len__(self):
        return self.length
    
    def insertFront(self, data):
        node = Node(data)                   # 새 노드 생성
        if self.head is None:               # 기존 노드가 없을 때
            self.head = node                # 새 노드가 첫 노드이므로 head에 새 노드 할당
        else:                               # 기존 노드가 있을 때
            node.next = self.head           # 새 노드의 next가 head를 가리키도록 한다.
            self.head = node                # head를 새 노드로 옮긴다.
        self.length += 1                    # linked list의 길이 1 증가

    def insertTail(self, data):
        node = Node(data)                   # 새 노드 생성
        if self.head is None:               # 기존 노드가 없을 때
            self.head = node                # 새 노드가 첫 노드이므로 head에 새 노드 할당
        else:                               # 기존 노드가 있을 때
            prev = self.head                # 새 노드의 이전 노드(마지막 노드)를 찾기 위해 prev 변수 생성
            while prev.next:                # head부터 마지막까지 이동
                prev = prev.next    
            prev.next = node                # prev의 next가 새 노드를 가리키도록 한다.
        self.length += 1                    # linked list의 길이 1 증가

    def display(self):
        if self.head is None:
            print("Empty")                  # 빈 리스트일 경우 "Empty" 출력
        else:
            node = self.head
            while node.next:
                print(node.data, end = ' → ')
                node = node.next
            print(node.data)                # 마지막 node 출력

    def deleteFront(self):
        if self.head is None:               # 빈 리스트일 경우 "None" 반환
            return None
        node = self.head                    # 노드 변수를 만들고 head를 붙인다.
        self.head = self.head.next          # head를 head의 next가 가리키는 노드로 옮긴다.
        self.length -= 1                    # linked list의 길이 1 감소
        return node.data                    # 삭제된 노드의 data 반환
    
    def deleteTail(self):
        if self.head is None:               # 빈 리스트일 경우 "None" 반환
            return None             
        node = self.head                    # 노드 변수를 만들고 head를 붙인다.
        if self.head.next is None:          # 노드가 1개일 경우
            self.head = None
        else:                               # 노드가 2개 이상일 경우
            while node.next is not None:    
                prev = node
                node = node.next            # 마지막 노드까지 이동
            prev.next = None                # 이전 노드의 next가 None을 가리키게 한다.
        self.length -= 1                    # linked list의 길이 1 감소
        return node.data                    # 삭제된 노드의 data 반환
    
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def insert(self, i, data):
        if i <= 0:
            self.insertFront(data)
        elif i >= self.length:
            self.insertTail(data)
        else:
            prev = self.head                # 삽입할 이전 위치까지 이동할 변수를 만들고 head부터 이전 위치까지 이동
            for _ in range(i-1):
                prev = prev.next
            node = Node(data)               # 새 노드 생성
            node.next = prev.next           # 새 노드의 next가 이전노드(prev)의 next가 가리키는 곳을 가리키도록 한다.
            prev.next =node                 # 이전 노드(prev)의 next가 새 노드를 가리키도록 한다.
            self.length += 1                # linked list의 길이 1 증가

    def delete(self, data):
        if self.head.data == data:          # 삭제할 노드가 head일 때
            self.deleteFront()
        prev = self.head                    # 삭제할 노드가 head가 아닐 때 삭제할 노드의 이전 노드를 찾는다.
        while prev.next:                    
            if prev.next.data == data:
                prev.next = prev.next.next  # 이전 노드의 next가 삭제할 노드의 next가 가리키는 노드를 가리키도록 한다. 
                self.length -= 1            # linked list의 길이 1 감소
                return True
            prev = prev.next
        return False