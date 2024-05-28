from tkinter import *
from random import *
from time import *

window = Tk()
window.title('Sudoku')
window.iconbitmap('./images/fifapc.ico')

def fill(values):
    boxes = []

    for i in range(9):
        boxes.append([])
        for j in range(9):
            if values[i][j]:
                boxes[i].append(Label(window, text = values[i][j], padx = 7, pady = 5).grid(row = i, column = j))
            else:
                boxes[i].append(Entry(window, width = 3).grid(row = i, column = j))

def create(values):
    blank = []
    for i in range(70):
        randomRow = randint(0, 8)
        randomColumn = randint(0, 8)
        while not [randomRow, randomColumn] in blank:
            blank.append([randomRow, randomColumn])
            break
    for i in range(len(blank)):
        values[blank[i][0]][blank[i][1]] = ''

    fill(values)

def main():
    values = [[]]

    #fill first line
    for i in range(9):
        values[0].append(randint(1, 9))

    #create other lines
    for i in range(1, 9):
        values.append([])
        for j in range(9):
            values[i].append(0)

    #check for repeated integer in first line
    for i in range(9):
        while values[0].count(values[0][i]) > 1:
            values[0][i] = randint(1, 9)

    #fill second line in the first box
    for i in range(3):
        while [values[0][0], values[0][1], values[0][2], values[1][0], values[1][1], values[1][2]].count(values[1][i]) > 1 or values[1][i] == 0:
            values[1][i] = randint(1, 9)

    rem = []

    for i in range(1, 10):
        if not i in [values[0][0], values[0][1], values[0][2], values[1][0], values[1][1], values[1][2]]:
            rem.append(i)

    #fill third line in first box
    for i in range(3):
        values[2][i] = rem[i]

    #fill second line in second box
    for i in range(3, 6):
        while [values[0][3], values[0][4], values[0][5], values[1][0], values[1][1], values[1][2], values[1][3], values[1][4], values[1][5]].count(values[1][i]) > 1 or values[1][i] == 0:
            values[1][i] = randint(1, 9)

    rem = []

    for i in range(3):
        if not values[2][i] in [values[0][3], values[0][4], values[0][5], values[1][3], values[1][4], values[1][5]]:
            rem.append(values[2][i])

    for i in range(len(rem)):
        values[1][i + 3] = rem[i]

    #fill third line in second box
    rem = []

    for i in range(1, 10):
        if not i in [values[0][3], values[0][4], values[0][5], values[1][3], values[1][4], values[1][5]]:
            rem.append(i)

    for i in range(3):
        values[2][i + 3] = rem[i]

    #fill second line in third box
    rem = []

    for i in range(1, 10):
        if not i in [values[1][0], values[1][1], values[1][2], values[1][3], values[1][4], values[1][5]]:
            rem.append(i)

    for i in range(3):
        values[1][i + 6] = rem[i]

    #fill third line in third box
    rem = []

    for i in range(1, 10):
        if not i in [values[2][0], values[2][1], values[2][2], values[2][3], values[2][4], values[2][5]]:
            rem.append(i)

    for i in range(3):
        values[2][i + 6] = rem[i]

    #fill fourth line
    for i in range(4):
        while values[3][i] in [values[0][i], values[1][i], values[2][i], 0] or values[3].count(values[3][i]) > 1:
            values[3][i] = randint(1, 9)

    rem = []

    for i in range(1, 10):
        if not i in values[3]:
            rem.append(i)

    combination = []

    for i in range(5):
        for j in range(5):
            while not j == i:
                for k in range(5):
                    while not (k == i or k == j):
                        for l in range(5):
                            while not (l == i or l == j or l == k):
                                for m in range(5):
                                    while not (m == i or m == j or m == k or m == l):
                                        combination.append([i, j, k, l, m])
                                        break
                                break
                        break
                break

    counter, error = 0, 0
    while values[3][4] in [values[0][4], values[1][4], values[2][4], 0] or values[3][5] in [values[0][5], values[1][5], values[2][5], 0] or values[3][6] in [values[0][6], values[1][6], values[2][6], 0] or values[3][7] in [values[0][7], values[1][7], values[2][7], 0] or values[3][8] in [values[0][8], values[1][8], values[2][8], 0]:
        values[3][4], values[3][5], values[3][6], values[3][7], values[3][8] = rem[combination[counter][0]], rem[combination[counter][1]], rem[combination[counter][2]], rem[combination[counter][3]], rem[combination[counter][4]]
        counter += 1
        if counter > 118:
            break

    #fill fifth line
    for i in range(5, 9):
        if i == 5:
            while values[4][i] in [values[0][i], values[1][i], values[2][i], values[3][3], values[3][4], values[3][5], 0] or values[4].count(values[4][i]) > 1:
                values[4][i] = randint(1, 9)
        else:
            while values[4][i] in [values[0][i], values[1][i], values[2][i], values[3][6], values[3][7], values[3][8], 0] or values[4].count(values[4][i]) > 1:
                values[4][i] = randint(1, 9)

    rem = []

    for i in range(1, 10):
        if not i in values[4]:
            rem.append(i)

    counter = 0
    while values[4][0] in [values[0][0], values[1][0], values[2][0], values[3][0], values[3][1], values[3][2], 0] or values[4][1] in [values[0][1], values[1][1], values[2][1], values[3][0], values[3][1], values[3][2], 0] or values[4][2] in [values[0][2], values[1][2], values[2][2], values[3][0], values[3][1], values[3][2], 0] or values[4][3] in [values[0][3], values[1][3], values[2][3], values[3][3], values[3][4], values[3][5], 0] or values[4][4] in [values[0][4], values[1][4], values[2][4], values[3][3], values[3][4], values[3][5], 0]:
        values[4][0], values[4][1], values[4][2], values[4][3], values[4][4] = rem[combination[counter][0]], rem[combination[counter][1]], rem[combination[counter][2]], rem[combination[counter][3]], rem[combination[counter][4]]
        counter += 1
        if counter > 118:
            break

    #fill sixth line
    combination1 = []

    for i in range(3):
        for j in range(3):
            while not j == i:
                for k in range(3):
                    while not (k == i or k == j):
                        combination1.append([i, j, k])
                        break
                break

    rem = []

    for i in range(1, 10):
        if not i in [values[3][0], values[3][1], values[3][2], values[4][0], values[4][1], values[4][2]]:
            rem.append(i)

    counter = 0
    while values[5][0] in [values[0][0], values[1][0], values[2][0], values[3][0], values[4][0], 0] or values[5][1] in [values[0][1], values[1][1], values[2][1], values[3][1], values[4][1], 0] or values[5][2] in [values[0][2], values[1][2], values[2][2], values[3][2], values[4][2], 0]:
        values[5][0], values[5][1], values[5][2] = rem[combination1[counter][0]], rem[combination1[counter][1]], rem[combination1[counter][2]]
        counter += 1
        if counter > 5:
            error += 1
            break

    rem = []

    for i in range(1, 10):
        if not i in [values[3][3], values[3][4], values[3][5], values[4][3], values[4][4], values[4][5]]:
            rem.append(i)

    counter = 0
    while values[5][3] in [values[0][3], values[1][3], values[2][3], values[3][3], values[4][3], 0] or values[5][4] in [values[0][4], values[1][4], values[2][4], values[3][4], values[4][4], 0] or values[5][5] in [values[0][5], values[1][5], values[2][5], values[3][5], values[4][5], 0]:
        values[5][3], values[5][4], values[5][5] = rem[combination1[counter][0]], rem[combination1[counter][1]], rem[combination1[counter][2]]
        counter += 1
        if counter > 5:
            error += 1
            break

    rem = []

    for i in range(1, 10):
        if not i in [values[3][6], values[3][7], values[3][8], values[4][6], values[4][7], values[4][8]]:
            rem.append(i)

    counter = 0
    while values[5][6] in [values[0][6], values[1][6], values[2][6], values[3][6], values[4][6], 0] or values[5][7] in [values[0][7], values[1][7], values[2][7], values[3][7], values[4][7], 0] or values[5][8] in [values[0][8], values[1][8], values[2][8], values[3][8], values[4][8], 0]:
        values[5][6], values[5][7], values[5][8] = rem[combination1[counter][0]], rem[combination1[counter][1]], rem[combination1[counter][2]]
        counter += 1
        if counter > 5:
            error += 1
            break

    if not error:
        error = 0
        #fill seventh, eighth and ninth lines
        rem = []
        for i in range(9):
            rem.append([])
            for j in range(1, 10):
                if not j in [values[0][i], values[1][i], values[2][i], values[3][i], values[4][i], values[5][i]]:
                    rem[i].append(j)

        for i in range(9):
            counter = 0
            while values[6].count(values[6][i]) > 1 or values[7].count(values[7][i]) > 1 or values[8].count(values[8][i]) > 1 or 0 in [values[6][i], values[7][i], values[8][i]]:
                values[6][i], values[7][i], values[8][i] = rem[i][combination1[counter][0]], rem[i][combination1[counter][1]], rem[i][combination1[counter][2]]
                counter += 1
                if counter > 5:
                    error += 1
                    break
        if error:
            main()
        else:
            create(values)
    else:
        main()

main()

window.mainloop()
