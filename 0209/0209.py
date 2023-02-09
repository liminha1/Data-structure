# def isStackFull() :
#     global SIZE, stack, top
#     if top >= SIZE-1 :
#         return True
#     else :
#         return False

def push(data) :
    global SIZE, stack, top
    if top >= SIZE-1 :
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

SIZE = 5
stack = ["커커", "녹녹", "꿀꿀", "콜콜", None]
top = 3

print(stack)
push("환환")
print(stack)
push("게토게토")