def add_data(friend):
    '''
    선형 리스트의 맨 뒤에 원소 삽입
    :param friend: str
    :return: void
    '''

    katok.append(None)
    katok[-1] = friend
    # katok[len(katok) - 1] = friend

def insert_data(position, friend) :
    '''
    선형 리스트의 position 위치에 원소 삽입
    :param position: int
    :param friend: str
    :return: void
    '''

    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)  # 빈칸 추가

    for i in range(len(katok) - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend  # 지정한 위치에 친구 추가


def delete_data(position):
    '''
    선형 리스트의 position 위치의 원소 삭제
    :param position: int
    :return: void
    '''
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    katok[position] = None  # 데이터 삭제

    for i in range(position + 1, len(katok)):
        katok[i - 1] = katok[i]
        katok[i] = None  # 배열의 맨 마지막 위치 삭제

    del (katok[len(katok) - 1])


katok = []

if __name__ == "__main__":

    while True:

        select = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")

        if (select == '1') :
            data = input("추가할 데이터 --> ")
            add_data(data)
            print(katok)
        elif (select == '2') :
            pos = int(input("삽입할 위치 --> "))
            data = input("추가할 데이터 --> ")
            insert_data(pos, data)
            print(katok)
        elif (select == '3') :
            pos = int(input("삭제할 위치 --> "))
            delete_data(pos)
            print(katok)
        elif (select == '4') :
            print(katok)
            break
        else :
            print("1 ~ 4 중 하나를 입력하세요.")
            continue
