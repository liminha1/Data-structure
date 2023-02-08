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

    insertNode("다다", "화화")
    printNodes(head)

    insertNode("사사", "솔솔")
    printNodes(head)

    insertNode("재재", "문문")
    printNodes(head)
