class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None


def printNodes(start) :
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        print('# 첫 노드가 삭제됨 #')
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            print('# 중간 노드가 삭제됨 #')
            return

    print('# 삭제된 노드가 없음 #')



memory = []
head, current, pre = None, None, None
dataArray = ["다다", "정정", "쯔쯔", "사사", "지지"]

if __name__ == "__main__" :

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    deleteNode("다다")
    printNodes(head)

    deleteNode("쯔쯔")
    printNodes(head)

    deleteNode("지지")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)