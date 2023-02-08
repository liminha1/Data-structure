def printPoly(t_x, p_x) :
    '''
    다항식을 포맷에 맞게 출력하는 함수
    :param t_x: 차수를 원소로 가지고 있는 List
    :param p_x: 계수를 원소로 가지고 있는 List
    :return: 다항식 문자열
    '''
    polyStr = "P(x) = "

    for i in range(len(p_x)) :
        term = t_x[i]
        coef = p_x[i]

        if coef >= 0 :
            polyStr += "+"
        polyStr += f'{str(coef)}x^{str(term)} '

    return polyStr


def calcPoly(xval, t_x, p_x) :
    '''
    다항식의 산술 연산을 하는 함수
    :param xval: x값 integer
    :param t_x: 차수를 원소로 가지고 있는 List
    :param p_x: 계수를 원소로 가지고 있는 List
    :return: 다항식 계산 결과 값 integer
    '''
    retValue = 0

    for i in range(len(px)) :
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xval ** term

    return retValue


tx = [300, 20, 0]
px = [7, -4, 5]


if __name__ == "__main__" :

    print(printPoly(tx, px))

    # xValue = int(input("X 값 --> "))
    print(calcPoly(int(input("X 값 --> ")), tx, px))