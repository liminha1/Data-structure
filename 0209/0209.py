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

def deQueue() :
	global SIZE, queue, front, rear
	if isQueueEmpty() :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if isQueueEmpty():
		print("큐가 비었습니다.")
		return None
	return queue[front + 1]


SIZE = 5
queue = [ "화화", "솔솔", "문문", None, None]
front = -1
rear = 2

print(queue)
retData = peek()
print("다음에 추출될 데이터 확인 -->", retData)
print(queue)