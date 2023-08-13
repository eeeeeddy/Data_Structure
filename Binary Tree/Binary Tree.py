class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def searchMin(self):    # 이진 트리의 최솟값 찾기
        node = self.root
        while node.left:    # 제일 왼쪽 리프노드로 접근
            node = node.left
        return node

    def searchMax(self):    # 이진 트리의 최댓값 찾기
        node = self.root    
        while node.right:   # 제일 오른쪽 리프노드로 접근
            node = node.right
        return node

    def insert(self, data): # 이진 트리에 data 삽입
        node = Node(data)
        parent = None
        current = self.root

        while current:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

    def search(self, data):
        node = self.root
        while True:
            if node is None:
                return node
            elif node.data == data:
                return data
            elif data < node.data:
                node = node.left
            else:
                node = node.right

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node:
            self._inOrder(node.left)
            print(node.data, end = ' ')
            self._inOrder(node.right)

    def preOrder(self):
        self._preOrder(self.root)

    def _preOrder(self, node):
        if node:
            print(node.data, end = ' ')
            self._preOrder(node.left)
            self._preOrder(node.right)

    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.data, end = ' ')

tree = Tree()   # 이진 트리 생성
tree.insert(12)
tree.insert(5)
tree.insert(9)
tree.insert(2)
tree.insert(18)
tree.insert(19)
tree.insert(15)
tree.insert(17)
print("min: %s" % tree.searchMin().data)
print("max: %s" % tree.searchMax().data)

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i,found))

tree.inOrder()
print()
tree.reverseInorder()
print()
tree.preOrder()
print()
tree.postOrder()
print()