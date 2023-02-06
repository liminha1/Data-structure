def printPoly(p_x):
    '''
    다항식을 포맷에 맞게 출력하는 함수
    :param p_x: 계수를 원소로 가지고 있는 List
    :return: 다항식 문자열
    '''
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(p_x)) :
        coef = p_x[i]

        if i > 0 and coef > 0:
            polyStr += "+"
        elif coef == 0 :
            term -= 1
            continue
        polyStr += f'{str(coef)}x^{str(term)} '
        term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    '''
    다항식의 산술 연산을 하는 함수
    :param xVal: x값 integer
    :param p_x: 계수를 원소로 가지고 있는 List
    :return: 다항식 계산 결과 값 integer
    '''
    retValue = 0
    term = len(p_x) -1

    for i in range(len(px)) :
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue


px = [7, -4, 0, 5]


if __name__ == "__main__" :

    print(printPoly(px))

    xVal = int(input("X 값 --> "))
    print(calcPoly(xVal, px))