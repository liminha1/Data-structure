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

SIZE = 5
queue = ["화화", "솔솔", "문문", "휘휘", None]
front = -1
rear = 3

print(queue)
enQueue("선선")
print(queue)
enQueue("재재")