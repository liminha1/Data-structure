def i_t(tk, tv):
    to_tv = [total[i][1] for i in range(len(total))]
    to_tv.append(tv)
    to_tv.sort()
    to_tv.reverse()
    idx = to_tv.index(tv)

    total.append(None)
    for i in range(len(total)-1, idx, -1):
        total[i] = total[i-1]
        total[i-1] = None

    total[idx] = [tk, tv]


total = [['다현', 200], ['정연', 150], ['쯔위', 90], ['사나', 30], ['지효', 15]]

if __name__ == "__main__":
    while True:
        friend = input("추가할 친구 --> ")
        num = int(input("카톡 횟수 --> "))
        i_t(friend, num)
        print(total)
