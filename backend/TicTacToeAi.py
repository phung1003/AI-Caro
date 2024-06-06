import copy
from cmath import sqrt

import numpy as np


class State:
    def __init__(self, data=None):
        self.data = data
        self.N = data.shape[1]

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    def Print(self):
        sz = self.N
        for i in range(sz):
            for j in range(sz):
                if self.data[i, j] == 0:
                    print('_', end='')
                elif self.data[i, j] == 1:
                    print('o', end='')
                elif self.data[i, j] == 2:
                    print('x', end='')
            print()
        print('================================')


class Operate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Move(self, s, isPlayerFirst):
        x = self.x
        y = self.y
        sz = s.N
        if x < 0 or x >= sz:
            return None
        if s.data[x, y] != 0:
            return None

        res = 0
        for row in s.data:
            for value in row:
                if value != 0:
                    res += 1

        sn = s.clone()
        if isPlayerFirst == True:
            if res % 2 == 0:
                sn.data[x, y] = 1  # o - player
            else:
                sn.data[x, y] = 2  # x - AI
            return sn
        else:
            if res % 2 == 0:
                sn.data[x, y] = 2  # x - AI
            else:
                sn.data[x, y] = 1  # o - player
            return sn


def isEndNode(s):
    sz = s.N
    data = s.data
    for i in range(sz):  # Check cac hang (chuoi 5 => win)
        for j in range(sz - 5 + 1):
            if (data[i, j + 0] != 0 and data[i, j + 0] == data[i, j + 1] and data[i, j + 0] == data[i, j + 2]
                    and data[i, j + 0] == data[i, j + 3] and data[i, j + 0] == data[i, j + 4]):
                return True

    for j in range(sz):  # Check cac cot (chuoi 5 => win)
        for i in range(sz - 5 + 1):
            if (data[i + 0, j] != 0 and data[i + 0, j] == data[i + 1, j] and data[i + 0, j] == data[i + 2, j]
                    and data[i + 0, j] == data[i + 3, j] and data[i + 0, j] == data[i + 4, j]):
                return True

    for i in range(sz - 5 + 1):  # Duong cheo chinh
        if (data[i + 0, i + 0] != 0 and data[i + 0, i + 0] == data[i + 1, i + 1]
                and data[i + 0, i + 0] == data[i + 2, i + 2]
                and data[i + 0, i + 0] == data[i + 3, i + 3]
                and data[i + 0, i + 0] == data[i + 4, i + 4]):
            return True

    for i in range(1, sz - 5 + 1):  # Duoi duong cheo chinh
        for j in range(i, sz - 5 + 1):
            if (data[j + 0, j + 0 - i] != 0 and data[j + 0, j + 0 - i] == data[j + 1, j + 1 - i]
                    and data[j + 0, j + 0 - i] == data[j + 2, j + 2 - i]
                    and data[j + 0, j + 0 - i] == data[j + 3, j + 3 - i]
                    and data[j + 0, j + 0 - i] == data[j + 4, j + 4 - i]):
                return True

    for i in range(1, sz - 5 + 1):  # Tren duong cheo chinh
        for j in range(i, sz - 5 + 1):
            if (data[j + 0 - i, j + 0] != 0 and data[j + 0 - i, j + 0] == data[j + 1 - i, j + 1]
                    and data[j + 0 - i, j + 0] == data[j + 2 - i, j + 2]
                    and data[j + 0 - i, j + 0] == data[j + 3 - i, j + 3]
                    and data[j + 0 - i, j + 0] == data[j + 4 - i, j + 4]):
                return True

    for i in range(sz - 5 + 1):  # Duong cheo phu
        if (data[i + 0, sz - 1 - (i + 0)] != 0 and data[i + 0, sz - 1 - (i + 0)] == data[i + 1, sz - 1 - (i + 1)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 2, sz - 1 - (i + 2)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 3, sz - 1 - (i + 3)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 4, sz - 1 - (i + 4)]):
            return True

    for i in range(1, sz - 5 + 1):  # Duoi duong cheo phu
        for j in range(i, sz - 5 + 1):
            if (data[j + 0, sz - (j + 0) + (i - 1)] != 0 and data[j + 0, sz - (j + 0) + (i - 1)] == data[
                j + 1, sz - (j + 1) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 2, sz - (j + 2) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 3, sz - (j + 3) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 4, sz - (j + 4) + (i - 1)]):
                return True

    for i in range(sz - 5):  # Tren duong cheo phu
        for j in range(sz - 5 - i):
            if (data[j + 0, sz - (2 + i) - (j + 0)] != 0 and data[j + 0, sz - (2 + i) - (j + 0)] == data[
                j + 1, sz - (2 + i) - (j + 1)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 2, sz - (2 + i) - (j + 2)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 3, sz - (2 + i) - (j + 3)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 4, sz - (2 + i) - (j + 4)]):
                return True

    for row in s.data:
        for value in row:
            if value == 0:
                return False
    return True


def Win(s):
    # if s.data == None:
    #     return False
    sz = s.N
    data = s.data
    for i in range(sz):  # Check cac hang (chuoi 5 => win)
        for j in range(sz - 5 + 1):
            if (data[i, j + 0] != 0 and data[i, j + 0] == data[i, j + 1] and data[i, j + 0] == data[i, j + 2]
                    and data[i, j + 0] == data[i, j + 3] and data[i, j + 0] == data[i, j + 4]):
                return True

    for j in range(sz):  # Check cac cot (chuoi 5 => win)
        for i in range(sz - 5 + 1):
            if (data[i + 0, j] != 0 and data[i + 0, j] == data[i + 1, j] and data[i + 0, j] == data[i + 2, j]
                    and data[i + 0, j] == data[i + 3, j] and data[i + 0, j] == data[i + 4, j]):
                return True

    for i in range(sz - 5 + 1):  # Duong cheo chinh
        if (data[i + 0, i + 0] != 0 and data[i + 0, i + 0] == data[i + 1, i + 1]
                and data[i + 0, i + 0] == data[i + 2, i + 2]
                and data[i + 0, i + 0] == data[i + 3, i + 3]
                and data[i + 0, i + 0] == data[i + 4, i + 4]):
            return True

    for i in range(1, sz - 5 + 1):  # Duoi duong cheo chinh
        for j in range(i, sz - 5 + 1):
            if (data[j + 0, j + 0 - i] != 0 and data[j + 0, j + 0 - i] == data[j + 1, j + 1 - i]
                    and data[j + 0, j + 0 - i] == data[j + 2, j + 2 - i]
                    and data[j + 0, j + 0 - i] == data[j + 3, j + 3 - i]
                    and data[j + 0, j + 0 - i] == data[j + 4, j + 4 - i]):
                return True

    for i in range(1, sz - 5 + 1):  # Tren duong cheo chinh
        for j in range(i, sz - 5 + 1):
            if (data[j + 0 - i, j + 0] != 0 and data[j + 0 - i, j + 0] == data[j + 1 - i, j + 1]
                    and data[j + 0 - i, j + 0] == data[j + 2 - i, j + 2]
                    and data[j + 0 - i, j + 0] == data[j + 3 - i, j + 3]
                    and data[j + 0 - i, j + 0] == data[j + 4 - i, j + 4]):
                return True

    for i in range(sz - 5 + 1):  # Duong cheo phu
        if (data[i + 0, sz - 1 - (i + 0)] != 0 and data[i + 0, sz - 1 - (i + 0)] == data[i + 1, sz - 1 - (i + 1)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 2, sz - 1 - (i + 2)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 3, sz - 1 - (i + 3)]
                and data[i + 0, sz - 1 - (i + 0)] == data[i + 4, sz - 1 - (i + 4)]):
            return True

    for i in range(1, sz - 5 + 1):  # Duoi duong cheo phu
        for j in range(i, sz - 5 + 1):
            if (data[j + 0, sz - (j + 0) + (i - 1)] != 0 and data[j + 0, sz - (j + 0) + (i - 1)] == data[
                j + 1, sz - (j + 1) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 2, sz - (j + 2) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 3, sz - (j + 3) + (i - 1)]
                    and data[j + 0, sz - (j + 0) + (i - 1)] == data[j + 4, sz - (j + 4) + (i - 1)]):
                return True

    for i in range(sz - 5):  # Tren duong cheo phu
        for j in range(sz - 5 - i):
            if (data[j + 0, sz - (2 + i) - (j + 0)] != 0 and data[j + 0, sz - (2 + i) - (j + 0)] == data[
                j + 1, sz - (2 + i) - (j + 1)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 2, sz - (2 + i) - (j + 2)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 3, sz - (2 + i) - (j + 3)]
                    and data[j + 0, sz - (2 + i) - (j + 0)] == data[j + 4, sz - (2 + i) - (j + 4)]):
                return True

    return False


def countRowWinCase(s, i, j, typeOfWinCase):  # TypeOfWinCase: x/o
    global opponent
    if typeOfWinCase == 'o':
        opponent = 2
    elif typeOfWinCase == 'x':
        opponent = 1

    sz = s.N
    data = s.data

    numOfWinCase = 0
    begin = 0
    end = 0

    # Xác định khoảng kiểm tra
    if j - 4 < 0:
        begin = 0
    else:
        begin = j - 4

    if j + 4 > sz - 1:
        end = sz - 5
    else:
        end = j

    for k in range(begin, end + 1):  # Check hàng ngang
        count = 0
        for m in range(5):
            if data[i, k + m] != opponent:
                count += 1
        if count == 5:
            numOfWinCase += 1

    return numOfWinCase


def countColumnWinCase(s, i, j, typeOfWinCase):  # TypeOfWinCase: x/o
    global opponent
    if typeOfWinCase == 'o':
        opponent = 2
    elif typeOfWinCase == 'x':
        opponent = 1
    sz = s.N
    data = s.data

    numOfWinCase = 0
    begin = 0
    end = 0

    # Xác định khoảng kiểm tra
    if i - 4 < 0:
        begin = 0
    else:
        begin = i - 4

    if i + 4 > sz - 1:
        end = sz - 5
    else:
        end = i

    for k in range(begin, end + 1):  # Check hàng ngang
        count = 0
        for m in range(5):
            if data[k + m, j] != opponent:
                count += 1
        if count == 5:
            numOfWinCase += 1

    return numOfWinCase


def countMainDiagonalWinCase(s, i, j, typeOfWinCase):  # TypeOfWinCase: x/o
    global opponent
    if typeOfWinCase == 'o':
        opponent = 2
    elif typeOfWinCase == 'x':
        opponent = 1

    sz = s.N
    data = s.data

    numOfWinCase = 0

    for k in range(5):
        if i - k < 0 or j - k < 0:
            break
        if i - k + 1 > sz - 1 or j - k + 1 > sz - 1:
            continue
        if i - k + 2 > sz - 1 or j - k + 2 > sz - 1:
            continue
        if i - k + 3 > sz - 1 or j - k + 3 > sz - 1:
            continue
        if i - k + 4 > sz - 1 or j - k + 4 > sz - 1:
            continue
        if (data[i - k, j - k] != opponent and data[i - k + 1, j - k + 1] != opponent
                and data[i - k + 2, j - k + 2] != opponent
                and data[i - k + 3, j - k + 3] != opponent
                and data[i - k + 4, j - k + 4] != opponent):
            numOfWinCase += 1

    return numOfWinCase


def countSecondaryDiagonalWinCase(s, i, j, typeOfWinCase):  # TypeOfWinCase: x/o
    global opponent
    if typeOfWinCase == 'o':
        opponent = 2
    elif typeOfWinCase == 'x':
        opponent = 1

    sz = s.N
    data = s.data

    numOfWinCase = 0
    for k in range(5):
        if i - k < 0 or j + k > sz - 1:
            break
        if i - k + 1 > sz - 1 or j + k - 1 < 0:
            continue
        if i - k + 2 > sz - 1 or j + k - 2 < 0:
            continue
        if i - k + 3 > sz - 1 or j + k - 3 < 0:
            continue
        if i - k + 4 > sz - 1 or j + k - 4 < 0:
            continue
        if (data[i - k, j + k] != opponent
                and data[i - k + 1, j + k - 1] != opponent
                and data[i - k + 2, j + k - 2] != opponent
                and data[i - k + 3, j + k - 3] != opponent
                and data[i - k + 4, j + k - 4] != opponent):
            numOfWinCase += 1

    return numOfWinCase


def evaluateWinPossibility(s, i, j, typeOfWinCase):  # typeOfWinCase: x/o
    # Hàng, cột, đường chéo chứa ô đang xét còn khả năng chứa chuỗi 5

    numOfWinCase = 0

    numOfWinCase += countRowWinCase(s, i, j, typeOfWinCase)
    numOfWinCase += countColumnWinCase(s, i, j, typeOfWinCase)
    numOfWinCase += countMainDiagonalWinCase(s, i, j, typeOfWinCase)
    numOfWinCase += countSecondaryDiagonalWinCase(s, i, j, typeOfWinCase)

    return numOfWinCase


def countSelectedBoxAroundInRow(s, i, j, typeOfSelectedBox):  # typeOfSelectedBox là x/o
    global opponentBox, selectedBox
    sz = s.N
    data = s.data

    if typeOfSelectedBox == 'x':
        opponentBox = 1
        selectedBox = 2
    elif typeOfSelectedBox == 'o':
        opponentBox = 2
        selectedBox = 1

    numOfSelectedBox = 0
    for k in range(1, 5):  # (i,j) -> right
        if j + k > sz - 1:
            break
        if data[i, j + k] == opponentBox:
            break
        if data[i, j + k] == selectedBox:
            numOfSelectedBox += 1

    for k in range(1, 5):  # (i,j) -> left
        if j - k < 0:
            break
        if data[i, j - k] == opponentBox:
            break
        if data[i, j - k] == selectedBox:
            numOfSelectedBox += 1

    return numOfSelectedBox


def countSelectedBoxAroundInColumn(s, i, j, typeOfSelectedBox):
    global opponentBox, selectedBox
    sz = s.N
    data = s.data

    if typeOfSelectedBox == 'x':
        opponentBox = 1
        selectedBox = 2
    elif typeOfSelectedBox == 'o':
        opponentBox = 2
        selectedBox = 1

    numOfSelectedBox = 0
    for k in range(1, 5):  # (i,j) -> bottom
        if i + k > sz - 1:
            break
        if data[i + k, j] == opponentBox:
            break
        if data[i + k, j] == selectedBox:
            numOfSelectedBox += 1

    for k in range(1, 5):  # (i,j) -> top
        if i - k < 0:
            break
        if data[i - k, j] == opponentBox:
            break
        if data[i - k, j] == selectedBox:
            numOfSelectedBox += 1

    return numOfSelectedBox


def countSelectBoxAroundInMainDiagonal(s, i, j, typeOfSelectedBox):
    global opponentBox, selectedBox
    sz = s.N
    data = s.data

    if typeOfSelectedBox == 'x':
        opponentBox = 1
        selectedBox = 2
    elif typeOfSelectedBox == 'o':
        opponentBox = 2
        selectedBox = 1

    numOfSelectedBox = 0
    for k in range(1, 5):  # (i,j) -> (i + k, j + k)
        if i + k > sz - 1 or j + k > sz - 1:
            break
        if data[i + k, j + k] == opponentBox:
            break
        if data[i + k, j + k] == selectedBox:
            numOfSelectedBox += 1

    for k in range(1, 5):  # (i,j) -> (i - k, j - k)
        if i - k < 0 or j - k < 0:
            break
        if data[i - k, j - k] == opponentBox:
            break
        if data[i - k, j - k] == selectedBox:
            numOfSelectedBox += 1

    return numOfSelectedBox


def countSelectedBoxAroundInSecondaryDiagonal(s, i, j, typeOfSelectedBox):
    global opponentBox, selectedBox
    sz = s.N
    data = s.data

    if typeOfSelectedBox == 'x':
        opponentBox = 1
        selectedBox = 2
    elif typeOfSelectedBox == 'o':
        opponentBox = 2
        selectedBox = 1

    numOfSelectedBox = 0
    for k in range(1, 5):  # (i,j) -> (i - k, j + k)
        if i - k < 0 or j + k > sz - 1:
            break
        if data[i - k, j + k] == opponentBox:
            break
        if data[i - k, j + k] == selectedBox:
            numOfSelectedBox += 1

    for k in range(1, 5):  # (i,j) -> (i + k, j - k)
        if i + k > sz - 1 or j - k < 0:
            break
        if data[i + k, j - k] == opponentBox:
            break
        if data[i + k, j - k] == selectedBox:
            numOfSelectedBox += 1

    return numOfSelectedBox


def countSelectedBoxAround(s, i, j, typeOfSelectedBox):  # typeOfSelectedBox là x/o
    numOfSelectedBox = 0

    numOfSelectedBox += countSelectedBoxAroundInRow(s, i, j, typeOfSelectedBox)
    numOfSelectedBox += countSelectedBoxAroundInColumn(s, i, j, typeOfSelectedBox)
    numOfSelectedBox += countSelectBoxAroundInMainDiagonal(s, i, j, typeOfSelectedBox)
    numOfSelectedBox += countSelectedBoxAroundInSecondaryDiagonal(s, i, j, typeOfSelectedBox)

    return numOfSelectedBox


def examineRow(s, i, j, typeOfWinCase):
    sz = s.N
    data = s.data

    global opponent, winType
    if typeOfWinCase == 'x':
        winType = 2
        opponent = 1
    elif typeOfWinCase == 'o':
        winType = 1
        opponent = 2

    count = 0
    if j - 3 >= 0 and j + 2 <= sz - 1:
        if (data[i, j - 3] != opponent
                and data[i, j - 2] == winType
                and data[i, j - 1] == winType
                and data[i, j + 1] != opponent
                and data[i, j + 2] != opponent):
            count += 1

    if j - 2 >= 0 and j + 3 <= sz - 1:
        if (data[i, j - 2] != opponent
                and data[i, j - 1] != opponent
                and data[i, j + 1] == winType
                and data[i, j + 2] == winType
                and data[i, j + 3] != opponent):
            count += 1

    if count >= 1:
        return 1
    else:
        return 0


def examineColumn(s, i, j, typeOfWinCase):
    sz = s.N
    data = s.data

    global opponent, winType
    if typeOfWinCase == 'x':
        winType = 2
        opponent = 1
    elif typeOfWinCase == 'o':
        winType = 1
        opponent = 2

    count = 0
    if i - 3 >= 0 and i + 2 <= sz - 1:
        if (data[i - 3, j] != opponent
                and data[i - 2, j] == winType
                and data[i - 1, j] == winType
                and data[i + 1, j] != opponent
                and data[i + 2, j] != opponent):
            count += 1
    if i - 2 >= 0 and i + 3 <= sz - 1:
        if (data[i - 2, j] != opponent
                and data[i - 1, j] != opponent
                and data[i + 1, j] == winType
                and data[i + 2, j] == winType
                and data[i + 3, j] != opponent):
            count += 1

    if count >= 1:
        return 1
    else:
        return 0


def examineMainDiagonal(s, i, j, typeOfWinCase):
    sz = s.N
    data = s.data

    global opponent, winType
    if typeOfWinCase == 'x':
        winType = 2
        opponent = 1
    elif typeOfWinCase == 'o':
        winType = 1
        opponent = 2

    count = 0
    if i - 3 >= 0 and j - 3 >= 0 and i + 2 <= sz - 1 and j + 2 <= sz - 1:
        if (data[i - 3, j - 3] != opponent
                and data[i - 2, j - 2] == winType
                and data[i - 1, j - 1] == winType
                and data[i + 1, j + 1] != opponent
                and data[i + 2, j + 2] != opponent):
            count += 1
    if i - 2 >= 0 and j - 2 >= 0 and i + 3 <= sz - 1 and j + 3 <= sz - 1:
        if (data[i - 2, j - 2] != opponent
                and data[i - 1, j - 1] != opponent
                and data[i + 1, j + 1] == winType
                and data[i + 2, j + 2] == winType
                and data[i + 3, j + 3] != opponent):
            count += 1

    if count >= 1:
        return 1
    else:
        return 0


def examineSecondaryDiagonal(s, i, j, typeOfWinCase):
    sz = s.N
    data = s.data

    global opponent, winType
    if typeOfWinCase == 'x':
        winType = 2
        opponent = 1
    elif typeOfWinCase == 'o':
        winType = 1
        opponent = 2

    count = 0
    if i - 3 >= 0 and j + 3 <= sz - 1 and i + 2 <= sz - 1 and j - 2 >= 0:
        if (data[i - 3, j + 3] != opponent
                and data[i - 2, j + 2] == winType
                and data[i - 1, j + 1] == winType
                and data[i + 1, j - 1] != opponent
                and data[i + 2, j - 2] != opponent):
            count += 1
    if i - 2 >= 0 and j + 2 < sz - 1 and j - 3 >= 0 and i + 3 <= sz - 1:
        if (data[i - 2, j + 2] != opponent
                and data[i - 1, j + 1] != opponent
                and data[i + 1, j - 1] == winType
                and data[i + 2, j - 2] == winType
                and data[i + 3, j - 3] != opponent):
            count += 1

    if count >= 1:
        return 1
    else:
        return 0


def doubleWinCase(s, i, j, typeOfWinCase):
    count = 0
    count += examineRow(s, i, j, typeOfWinCase)
    count += examineColumn(s, i, j, typeOfWinCase)
    count += examineMainDiagonal(s, i, j, typeOfWinCase)
    count += examineSecondaryDiagonal(s, i, j, typeOfWinCase)

    if count >= 2:
        return 1
    else:
        return 0

def chainOf3WithEmptyAtBothEndsInColumn(s, i, j, typeOfChain):
    sz = s.N
    data = s.data

    global opponent, chainType
    if typeOfChain == 'x':
        chainType = 2
        opponent = 1
    elif typeOfChain == 'o':
        chainType = 1
        opponent = 2

    if i - 2 >= 0 and i + 2 <= sz - 1:  # TH1: _x_x_
        if (data[i + 1, j] == chainType
                and data[i - 1, j] == chainType
                and data[i + 2, j] == 0
                and data[i - 2, j] == 0):
            return 1

    if i + 3 <= sz - 1 and i - 1 >= 0:  # TH2: __xx_
        if (data[i + 1, j] == chainType
                and data[i + 2, j] == chainType
                and data[i - 1, j] == 0
                and data[i + 3, j] == 0):
            return 1

    if i - 3 >= 0 and i + 1 <= sz - 1:  # TH2: _xx__
        if (data[i - 1, j] == chainType
                and data[i - 2, j] == chainType
                and data[i - 3, j] == 0
                and data[i + 1, j] == 0):
            return 1

    return 0

def chainOf3WithEmptyAtBothEndsInRow(s, i, j, typeOfChain):
    sz = s.N
    data = s.data

    global opponent, chainType
    if typeOfChain == 'x':
        chainType = 2
        opponent = 1
    elif typeOfChain == 'o':
        chainType = 1
        opponent = 2

    if j - 2 >= 0 and j + 2 <= sz - 1:  # TH1: _x_x_
        if (data[i, j + 1] == chainType
                and data[i, j - 1] == chainType
                and data[i, j + 2] == 0
                and data[i, j - 2] == 0):
            return 1

    if j + 3 <= sz - 1 and j - 1 >= 0:  # TH2: __xx_
        if (data[i, j + 1] == chainType
                and data[i, j + 2] == chainType
                and data[i, j - 1] == 0
                and data[i, j + 3] == 0):
            return 1

    if j - 3 >= 0 and j + 1 <= sz - 1:  # TH2: _xx__
        if (data[i, j - 1] == chainType
                and data[i, j - 2] == chainType
                and data[i, j - 3] == 0
                and data[i, j + 1] == 0):
            return 1

    return 0


def chainOf3WithEmptyAtBothEndsInMainDiagonal(s, i, j, typeOfChain):
    sz = s.N
    data = s.data

    global opponent, chainType
    if typeOfChain == 'x':
        chainType = 2
        opponent = 1
    elif typeOfChain == 'o':
        chainType = 1
        opponent = 2

    if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= sz - 1 and j + 2 <= sz - 1:  # TH1: _x_x_
        if (data[i - 1, j - 1] == chainType
                and data[i + 1, j + 1] == chainType
                and data[i - 2, j - 2] == 0
                and data[i + 2, j + 2] == 0):
            return 1

    if i - 3 >= 0 and j - 3 >= 0 and i + 1 <= sz - 1 and j + 1 <= sz - 1:  # TH2: _xx__
        if (data[i - 1, j - 1] == chainType
                and data[i - 2, j - 2] == chainType
                and data[i - 3, j - 3] == 0
                and data[i + 1, j + 1] == 0):
            return 1

    if i + 3 <= sz - 1 and j + 3 <= sz - 1 and i - 1 >= 0 and j - 1 >= 0:  # TH3: __xx_
        if (data[i + 1, j + 1] == chainType
                and data[i + 2, j + 2] == chainType
                and data[i + 3, j + 3] == 0
                and data[i - 1, j - 1] == 0):
            return 1

    return 0


def chainOf3WithEmptyAtBothEndsInSecondaryDiagonal(s, i, j, typeOfChain):
    sz = s.N
    data = s.data

    global opponent, chainType
    if typeOfChain == 'x':
        chainType = 2
        opponent = 1
    elif typeOfChain == 'o':
        chainType = 1
        opponent = 2

    if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= sz - 1 and j + 2 <= sz - 1:  # TH1: _x_x_
        if (data[i + 1, j - 1] == chainType
                and data[i - 1, j + 1] == chainType
                and data[i + 2, j - 2] == 0
                and data[i - 2, j + 2] == 0):
            return 1

    if i + 3 <= sz - 1 and j - 3 >= 0 and i - 1 >= 0 and j + 1 <= sz - 1:  # TH2: _xx__
        if (data[i + 1, j - 1] == chainType
                and data[i + 2, j - 2] == chainType
                and data[i + 3, j - 3] == 0
                and data[i - 1, j + 1] == 0):
            return 1

    if i - 3 >= 0 and j + 3 <= sz - 1 and i + 1 <= sz - 1 and j - 1 >= 0:  # TH3: __xx_
        if (data[i - 1, j + 1] == chainType
                and data[i - 2, j + 2] == chainType
                and data[i - 3, j + 3] == 0
                and data[i + 1, j - 1] == 0):
            return 1

    return 0


def countChainOf3WithEmptyAtBothEnds(s, i, j, typeOfChain):
    countChainOf3 = (chainOf3WithEmptyAtBothEndsInRow(s, i, j, typeOfChain)
                     + chainOf3WithEmptyAtBothEndsInColumn(s, i, j, typeOfChain)
                     + chainOf3WithEmptyAtBothEndsInMainDiagonal(s, i, j, typeOfChain)
                     + chainOf3WithEmptyAtBothEndsInSecondaryDiagonal(s, i, j, typeOfChain))

    return countChainOf3


def distanceFromCenter(s, i, j):
    sz = s.N
    center = (int)(sz/2)

    return abs((sz/2)*(sz/2) - (abs(center-i)*abs(center-i) + abs(center - j)*abs(center-j)))


def heuristicFunc(s, i, j):

    if doubleWinCase(s, i, j, 'x') == 1:
        heuristic = 10
        return -heuristic/100
    if doubleWinCase(s, i, j, 'o') == 1:
        heuristic = 9
        return -heuristic/100
    if countChainOf3WithEmptyAtBothEnds(s, i, j, 'x'):
        heuristic = 8 + countChainOf3WithEmptyAtBothEnds(s, i, j, 'x')/10
        return -heuristic/100
    if countChainOf3WithEmptyAtBothEnds(s, i, j, 'o'):
        heuristic = 7 + countChainOf3WithEmptyAtBothEnds(s, i, j, 'o')/10
        return -heuristic/100
    else:
        winPossibilityHeuristic = evaluateWinPossibility(s, i, j, 'x')
        selectedBoxAroundHeuristic = countSelectedBoxAround(s, i, j, 'x')
        heuristic = winPossibilityHeuristic + 1.2 * selectedBoxAroundHeuristic + distanceFromCenter(s, i, j)/10
        return -heuristic/1000


def checkMyTurn(s, isPlayerFirst):
    res = 0

    for row in s.data:
        for x in row:
            if x != 0:
                res += 1

    if isPlayerFirst:
        res += 1  # res += 1 để dự đoán nước đi sau

    if res % 2 == 0:
        return True
    return False


def Value(s, isPlayerFirst):
    if Win(s):
        if checkMyTurn(s, isPlayerFirst):
            return 1
        return -1
    return 0


def AlphaBeta(s, d, a, b, mp, isPlayerFirst):  # s, depth, alpha, beta, Maximum Player
    if isEndNode(s) or d == 0:
        return Value(s, isPlayerFirst)
    sz = s.N
    border = determineMinimaxBorder(s)

    if mp == True:  # Maximum Player
        for i in range(border.beginI, border.endI + 1):
            for j in range(border.beginJ, border.endJ + 1):
                if isNecessaryToCheckMiniMax(s, i, j) == False:
                    continue
                child = Operate(i, j).Move(s, isPlayerFirst)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, False, isPlayerFirst)
                a = max(a, tmp)
                if a >= b:
                    break
        return a
    else:
        for i in range(border.beginI, border.endI + 1):
            for j in range(border.beginJ, border.endJ + 1):
                child = Operate(i, j).Move(s, isPlayerFirst)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, True, isPlayerFirst)
                b = min(b, tmp)
                if a >= b:
                    break
        return b


def MiniMax(s, d, mp, isPlayerFirst):
    return AlphaBeta(s, d, -2, 2, mp, isPlayerFirst)


def choosePlayTurn():
    option = int(input("Who plays first(1-Player/0-AI)?: "))
    if option == 1:
        isPlayerFirst = True
    else:
        isPlayerFirst = False

    return isPlayerFirst


class MinimaxBorder:
    def __init__(self, beginI=None, endI=None, beginJ=None, endJ=None):
        self.beginI = (int)(beginI)
        self.endI = (int)(endI)
        self.beginJ = (int)(beginJ)
        self.endJ = (int)(endJ)


def countSelectedBox(s):
    res = 0

    for row in s.data:
        for x in row:
            if x != 0:
                res += 1
    return res


def determineMinimaxBorder(s):
    sz = s.N
    data = s.data
    if countSelectedBox(s) <= 4:
        begin = (sz - 1) / 2 - 2
        end = (sz - 1) / 2 + 2
        border = MinimaxBorder(beginI=begin, beginJ=begin, endI=end, endJ=end)
        return border

    else:
        beginI = (sz - 1) / 2
        endI = (sz - 1) / 2
        beginJ = (sz - 1) / 2
        endJ = (sz - 1) / 2
        for i in range(sz):
            for j in range(sz):
                if data[i, j] != 0:
                    beginI = min(beginI, i)
                    endI = max(endI, i)
                    beginJ = min(beginJ, j)
                    endJ = max(endJ, j)
        if beginI > 0: beginI -= 1
        if endI < sz - 1: endI += 1
        if beginJ > 0: beginJ -= 1
        if endJ < sz - 1: endJ += 1
        border = MinimaxBorder(beginI=beginI, beginJ=beginJ, endI=endI, endJ=endJ)
        return border


def examineAroundBoxInRow(s, i, j):
    sz = s.N
    data = s.data

    numOfX = 0
    # 1 - o - player
    # 2 - x - AI
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi x dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> right
        if j + k > sz - 1:
            break
        if data[i, j + k] == 1:
            break
        if data[i, j + k] == 2:
            numOfX += 1

    for k in range(1, 3):  # (i,j) -> left
        if j - k < 0:
            break
        if data[i, j - k] == 1:
            break
        if data[i, j - k] == 2:
            numOfX += 1

    numOfO = 0
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi o dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> right
        if j + k > sz - 1:
            break
        if data[i, j + k] == 2:
            break
        if data[i, j + k] == 1:
            numOfO += 1

    for k in range(1, 3):  # (i,j) -> left
        if j - k < 0:
            break
        if data[i, j - k] == 2:
            break
        if data[i, j - k] == 1:
            numOfO += 1

    if numOfX >= 2 or numOfO >= 2:
        return True
    else:
        return False


def examineAroundBoxInColumn(s, i, j):
    sz = s.N
    data = s.data

    numOfX = 0
    # 1 - o - player
    # 2 - x - AI
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi x dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> bottom
        if i + k > sz - 1:
            break
        if data[i + k, j] == 1:
            break
        if data[i + k, j] == 2:
            numOfX += 1

    for k in range(1, 3):  # (i,j) -> top
        if i - k < 0:
            break
        if data[i - k, j] == 1:
            break
        if data[i - k, j] == 2:
            numOfX += 1

    numOfO = 0
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi o dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> bottom
        if i + k > sz - 1:
            break
        if data[i + k, j] == 2:
            break
        if data[i + k, j] == 1:
            numOfO += 1

    for k in range(1, 3):  # (i,j) -> top
        if i - k < 0:
            break
        if data[i - k, j] == 2:
            break
        if data[i - k, j] == 1:
            numOfO += 1

    if numOfX >= 2 or numOfO >= 2:
        return True
    else:
        return False


def examineAroundBoxInMainDiagonal(s, i, j):
    sz = s.N
    data = s.data

    numOfX = 0
    # 1 - o - player
    # 2 - x - AI
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi x dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> (i + k, j + k)
        if i + k > sz - 1 or j + k > sz - 1:
            break
        if data[i + k, j + k] == 1:
            break
        if data[i + k, j + k] == 2:
            numOfX += 1

    for k in range(1, 3):  # (i,j) -> (i - k, j - k)
        if i - k < 0 or j - k < 0:
            break
        if data[i - k, j - k] == 1:
            break
        if data[i - k, j - k] == 2:
            numOfX += 1

    numOfO = 0
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi o dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> (i + k, j + k)
        if i + k > sz - 1 or j + k > sz - 1:
            break
        if data[i + k, j + k] == 2:
            break
        if data[i + k, j + k] == 1:
            numOfO += 1

    for k in range(1, 3):  # (i,j) -> (i - k, j - k)
        if i - k < 0 or j - k < 0:
            break
        if data[i - k, j - k] == 2:
            break
        if data[i - k, j - k] == 1:
            numOfO += 1

    if numOfX >= 2 or numOfO >= 2:
        return True
    else:
        return False


def examineAroundBoxInSecondaryDiagonal(s, i, j):
    sz = s.N
    data = s.data

    numOfX = 0
    # 1 - o - player
    # 2 - x - AI
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi x dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> (i - k, j + k)
        if i - k < 0 or j + k > sz - 1:
            break
        if data[i - k, j + k] == 1:
            break
        if data[i - k, j + k] == 2:
            numOfX += 1

    for k in range(1, 3):  # (i,j) -> (i + k, j - k)
        if i + k > sz - 1 or j - k < 0:
            break
        if data[i + k, j - k] == 1:
            break
        if data[i + k, j - k] == 2:
            numOfX += 1

    numOfO = 0
    # kiểm tra 2 ô bên cạnh (i,j)-trống có chứa chuỗi o dài bao nhiêu?
    for k in range(1, 3):  # (i,j) -> (i - k, j + k)
        if i - k < 0 or j + k > sz - 1:
            break
        if data[i - k, j + k] == 2:
            break
        if data[i - k, j + k] == 1:
            numOfO += 1

    for k in range(1, 3):  # (i,j) -> (i + k, j - k)
        if i + k > sz - 1 or j - k < 0:
            break
        if data[i + k, j - k] == 2:
            break
        if data[i + k, j - k] == 1:
            numOfO += 1

    if numOfX >= 2 or numOfO >= 2:
        return True
    else:
        return False


def isNecessaryToCheckMiniMax(s, i, j):
    if examineAroundBoxInRow(s, i, j):
        return True
    if examineAroundBoxInColumn(s, i, j):
        return True
    if examineAroundBoxInMainDiagonal(s, i, j):
        return True
    if examineAroundBoxInSecondaryDiagonal(s, i, j):
        return True
    else:
        return False


class TictactoeMove:
    def __init__(self, checkMinimax=None, i=None, j=None, evaluationScore=None):
        self.checkMinimax = bool(checkMinimax)
        self.i = int(i)
        self.j = int(j)
        self.evaluationScore = evaluationScore

    def Print(self):
        print(self.checkMinimax, end=' ')
        print(self.i, end=' ')
        print(self.j, end=' ')
        print(self.evaluationScore)


def determineMinMove(list, isWin):
    for val in list:
        val.Print()

    if isWin:
        lastVal = list[-1]
        return lastVal

    endNode = False
    for val in list:
        if val.checkMinimax == True and val.evaluationScore == 1:
            endNode = True
            break

    if endNode == False:
        minMove = None
        mn = 2
        for val in list:
            if val.evaluationScore < mn:
                mn = val.evaluationScore
                minMove = val
        return minMove
    else:
        minMove = None
        mn = 2
        for val in list:
            if val.evaluationScore < mn and val.checkMinimax == True:
                mn = val.evaluationScore
                minMove = val
        return minMove

def changeBoardToInt(board, size):
    size = int(size)
    int_board = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'o':
                int_board[i][j] = 1
            if board[i][j] == 'x':
                int_board[i][j] = 2
    return int_board 


def RUN(board, isPlayerFirst, size):
    player = 1
    turn = 0
    N = int(size)
    iboard = changeBoardToInt(board=board, size=N)
    s = State(data=iboard)

    isPlayerFirst = isPlayerFirst
    if isPlayerFirst:
        player = 0
    else:
        player = 1


    s.Print()
 
 # AI
    mn = 2
    minChild = None
    # sz = s.N
    border = determineMinimaxBorder(s)
    tictactoeMoveList = []

    isWin = False
    for i in range(border.beginI, border.endI + 1):
        for j in range(border.beginJ, border.endJ + 1):
            tmp = 0
            child = Operate(i, j).Move(s, isPlayerFirst)
            if child == None:
                continue

            checkMinimax = False
            if isNecessaryToCheckMiniMax(s, i, j):
                if evaluateWinPossibility(s,i,j,'o') > 0 or evaluateWinPossibility(s,i,j,'x') > 0:
                    checkMinimax = True
                    tmp = MiniMax(child, 3, True, isPlayerFirst)

            if tmp == 0:
                tmp = heuristicFunc(s, i, j)

            move = TictactoeMove(checkMinimax, i, j, tmp)
            tictactoeMoveList.append(move)

            if Win(child):
                isWin = True
                break
        if (isWin):
            break


    minMove = determineMinMove(tictactoeMoveList, isWin)
    minChild = Operate(minMove.i, minMove.j).Move(s, isPlayerFirst)
    diff_indices = np.where(s.data != minChild.data)
    first_diff_index = (diff_indices[0][0], diff_indices[1][0])
    s = minChild
    print(s.data)
    return first_diff_index
            
       

# def RUN(board, isPlayerFirst, size):
#     player = 1
#     turn = 0
#     N = int(size)
#     iboard = changeBoardToInt(board=board, size=N)
#     s = State(data=iboard)

#     isPlayerFirst = isPlayerFirst
#     if isPlayerFirst:
#         player = 0
#     else:
#         player = 1


#     s.Print()
#  # AI
#     mn = 2
#     minChild = None
#     # sz = s.N
#     border = determineMinimaxBorder(s)
#     tictactoeMoveList = []

#     isWin = False
#     for i in range(border.beginI, border.endI + 1):
#         for j in range(border.beginJ, border.endJ + 1):
#             tmp = 0
#             child = Operate(i, j).Move(s, isPlayerFirst)
#             if child == None:
#                 continue

#             checkMinimax = False
#             if isNecessaryToCheckMiniMax(s, i, j):
#                 checkMinimax = True
#                 tmp = MiniMax(child, 3, True, isPlayerFirst)

#             if tmp == 0:
#                 tmp = heuristicFunc(s, i, j)

#             move = TictactoeMove(checkMinimax, i, j, tmp)
#             tictactoeMoveList.append(move)

#             if Win(child):
#                 isWin = True
#                 break
#         if (isWin):
#             break
    
#     minMove = determineMinMove(tictactoeMoveList, isWin)
#     minChild = Operate(minMove.i, minMove.j).Move(s, isPlayerFirst)
#     diff_indices = np.where(s.data != minChild.data)
#     first_diff_index = (diff_indices[0][0], diff_indices[1][0])
#     s = minChild
#     print(s.data)
#     return first_diff_index
    
    


            
# def RUN(board, isPlayerFirst, size):
#     player = 1
#     turn = 0
#     N = int(size)
#     iboard = changeBoardToInt(board=board, size=N)
#     s = State(data=iboard)

#     isPlayerFirst = isPlayerFirst
#     if isPlayerFirst:
#         player = 0
#     else:
#         player = 1

 
#     mn = 2
#     minChild = None
#     #sz = s.N
#     border = determineMinimaxBorder(s)
#     tictactoeMoveList = []

#     isWin = False
#     for i in range(border.beginI, border.endI + 1):
#         for j in range(border.beginJ, border.endJ + 1):
#             tmp = 0
#             child = Operate(i, j).Move(s, isPlayerFirst)
#             if child == None:
#                 continue

#             checkMinimax = False
#             if isNecessaryToCheckMiniMax(s, i, j):
#                 checkMinimax = True
#                 tmp = MiniMax(child, 3, True, isPlayerFirst)

#             if tmp == 0:
#                 tmp = evaluateWinPossibility(s, i, j) + 0.5 * countXAround(s, i, j)

#             move = TictactoeMove(checkMinimax, i, j, tmp)
#             tictactoeMoveList.append(move)
#             if Win(child):
#                 isWin = True
#                 break
#         if (isWin):
#             break
#     minMove = determineMinMove(tictactoeMoveList, isWin)
#     minChild = Operate(minMove.i, minMove.j).Move(s, isPlayerFirst)
#     diff_indices = np.where(s.data != minChild.data)
#     first_diff_index = (diff_indices[0][0], diff_indices[1][0])
#     s = minChild
#     return first_diff_index
    
             
      
      


# def RUN(board):
#     player = 1
#     turn = 0
#     N = 15
#     iboard = changeBoardToInt(board=board, size=N)
#     s = State(data=iboard)
#     s.Print()
  
#          #AI
#     mn = 2 # (minimax, depth)
#     minChild = None
#     sz = s.N
#     for i in range(sz):
#         isWin = False
#         for j in range(sz):
#             child = Operate(i, j).Move(s)
#             if child == None:
#                 continue
#             tmp = MiniMax(child, 1, True)
#             if tmp == 0:
#                 tmp = evaluateWinPossibility(s, i, j)
#             print(i, j, tmp)
#             if mn >= tmp:
#                 mn = tmp
#                 minChild = child
#             if Win(minChild) == True:
#                 isWin = True
#                 break
#         if (isWin):
#             break
#     diff_indices = np.where(s.data != minChild.data)
#     first_diff_index = (diff_indices[0][0], diff_indices[1][0])
#     s = minChild
#     return first_diff_index
#     print(s.data)
#     if Win(s):
#         s.Print()
#         print('AI win')
        
        
# def RUN(board, isPlayerFirst, size):
#     player = 1
#     turn = 0
#     N = int(size)
#     iboard = changeBoardToInt(board=board, size=N)
#     s = State(data=iboard)
#     if isPlayerFirst:
#         player = 0
#     else:
#         player = 1
#     mn = 2
#     minChild = None
#     sz = s.N
#     for i in range(sz):
#         isWin = False
#         for j in range(sz):
#             child = Operate(i, j).Move(s, isPlayerFirst)
#             if child == None:
#                 continue
#             tmp = MiniMax(child, 3, True, isPlayerFirst)
#             if tmp == 0:
#                 tmp = evaluateWinPossibility(s, i, j)
#             print(i, j, tmp)
#             if mn > tmp:
#                 mn = tmp
#                 minChild = child
#                 if Win(minChild) == True:
#                     mn = tmp
#                     minChild = child
#                     isWin = True
#                     break
#         if (isWin):
#             break
#     diff_indices = np.where(s.data != minChild.data)
#     first_diff_index = (diff_indices[0][0], diff_indices[1][0])
#     s = minChild
#     return first_diff_index
