katok = ['다현', '정연', '쯔위', '사나', '지효']


def delete_data(position):

    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    for i in range(position, len(katok)):  # 10, 11 없어도 작동됨
        katok[i] = None   # i 부터 끝까지 None 처리

    for _ in range(len(katok), position, -1) :
        # katok[i-1] = katok[i]
        # katok[i] = None
        katok.pop()   # 끝부터 i까지 리스트 삭제

    # del(katok[len(katok) - 1])
    # katok.pop()

print(katok)
delete_data(1)
print(katok)
# delete_data(3)
# print(katok)

if __name__ == "__main__":
    katok = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(katok)
    delete_data(1)
    print(katok)
    delete_data(3)
    print(katok)