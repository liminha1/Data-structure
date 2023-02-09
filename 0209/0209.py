def isQueueFull() :
	global SIZE, queue, front, rear
	if rear == SIZE-1 :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if isQueueFull() :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if front == rear:
		return True
	else:
		return False

SIZE = 5
queue = [ None for _ in range(SIZE)]
front = -1
rear = -1

print("큐가 비었는지 여부 ==>", isQueueEmpty())