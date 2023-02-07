class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['검정분홍', '빨강', '아무무', '비분홍', '소년의날', '쌍둥이']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :

    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else:
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print("이진 탐색 트리 구성 완료!")