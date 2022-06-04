# Task-3
def LCS(X, Y, Z):
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1

    c = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]  # 3D matrix

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                else:
                    if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                        c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            maximum = c[i - 1][j][k]
                            if maximum >= c[i][j][k - 1]:
                                c[i][j][k] = maximum
                            else:
                                maximum = c[i][j][k - 1]
                                c[i][j][k] = maximum
                        else:
                            maximum = c[i][j - 1][k]
                            if maximum >= c[i][j][k - 1]:
                                c[i][j][k] = maximum
                            else:
                                maximum = c[i][j][k - 1]
                                c[i][j][k] = maximum

    return str(c[m - 1][n - 1][o - 1])


with open("task3-input.txt") as openFileobj:
    strings = openFileobj.read().split()

with open("task3-output.txt", "w") as outputFileObj:
    outputFileObj.write(LCS(strings[0], strings[1], strings[2]))

print("CODE EXECUTED!!!!!!!!!!!!!!!")
