katok = ["다현", "정연", "쯔위", "사나", "지효"]


def insert_data(position, friend) :

    if position < 0 or position > len(katok) :
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)

    for i in range(len(katok) - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

print(katok)
insert_data(2, '솔라')
print(katok)
insert_data(6, '문별')
print(katok)

if __name__ == "__main__":
	pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
	print(pokemons)
	pokemons.insert(3, '어니부기' )
	print(pokemons)
	pokemons.insert(6, '거북왕' )
	print(pokemons)
