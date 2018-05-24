# Quang Lam


def reduceGroups(groups):
    changed = False

    for i in range(len(groups)):
        g = groups[i]
        for j in range(len(g)):
            # Rule 1
            count = 0
            for z in range(len(g)):
                if g[z] == g[j]:
                    count = count + 1

            if len(g[j]) == count:
                for z in range(len(groups[i])):
                    if len(g[z]) > len(g[j]):
                       changed = True
                       g[z].difference_update(g[j])

            # Rule 2
            tmp = set(g[j])
            for num in g[j]:
                for z in range(len(g)):
                    if j != z and num in g[z]:
                        tmp.discard(num)
            if len(tmp) == 1:
                for num in set(g[j]):
                    if (num in tmp) != True:
                        g[j].discard(num)


    return changed


def printMatrix(matrix):
    for i in range (9):
        for j in range(9):
            if len(matrix[i][j]) > 1:
                print("x", end=" ")
            else:
                print(list(matrix[i][j])[0], end=" ")
        print()

def isValid(groups):
    for i in range(len(groups)):
        g = groups[i]

        checkList = set(range(1, 10))

        for j in range(len(g)):
            if len(g[j]) != 1: return False
            checkList.difference_update(g[j])

        if len(checkList) > 0: return False

    return True



def main():
    fileName = input("Please enter a Sodoku puzzle file name: ")

    # getMatrix
    infile = open(fileName, "r")

    table = []
    for line in infile:
        table.append(line.split())

    matrix = [[None for j in range(9)] for i in range(9)]
    for i in range (9):
        for j in range(9):
            if table[i][j] == 'x':
                matrix[i][j] = set(range(1, 10))
            else:
                matrix[i][j] = set([int(table[i][j])])

    infile.close()

    # Creating groups
    groups = []

    # rows
    for i in range(9):
        group = []
        for j in range(9):
            group.append(matrix[i][j])
        groups.append(group)

    # columns
    for i in range(9):
        group = []
        for j in range(9):
            group.append(matrix[j][i])
        groups.append(group)

    # square
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            group = []
            for i in range(3):
                for j in range(3):
                    group.append(matrix[i + n][j + m])
            groups.append(group)

    print("Solving this puzzle")
    print("-------------------")
    printMatrix(matrix)

    changed = True
    while changed:
        changed = reduceGroups(groups)

    print()
    print("Solution")
    print("-------------------")
    printMatrix(matrix)

    if isValid(groups):
        print()
        print("Valid solution!")


if __name__ == '__main__':
    main()