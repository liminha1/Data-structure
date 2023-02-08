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

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()

def makeSimpleLinkedList(namePhone) :
    global memory, head, current, pre
    printNodes(head)

    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None :
        head = node
        return

    if head.data[0] > namePhone[0] :
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] > namePhone[0]:
            pre.link = node
            node.link = current
            return

    current.link = node



memory = []
head, current, pre = None, None, None
dataArray = [["지지", "010-1111-1111"], ["정정", "010-2222-2222"], ["뷔뷔", "010-3333-3333"], ["슈슈", "010-4444-4444"], ["진진", "010-5555-5555"]]


if __name__ == "__main__" :

    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)