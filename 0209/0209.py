def isQueueFull() :
	global SIZE, queue, front, rear
	if reat == SIZE-1 :
		return True
	else :
		return False

SIZE = 5
queue = ["화화", "솔솔", "문문", "휘휘", "선선"]
front = -1
reat = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())
