def isStackFull() :
    global SIZE, stack, top
    if top >= SIZE-1 :
        return True
    else :
        return False

SIZE = 5
stack = ["커커", "녹녹", "꿀꿀", "콜콜", "환환"]
top = 4

print("스택이 꽉 찼는지 여부 ==>", isStackFull())