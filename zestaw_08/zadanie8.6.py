def funkcja_P(i, j):
    P = [0] * i
    for index in range (0, i):
        P[index] = [0] * j

    for index in range(0, j):
        if index == 0:
            P[0][index] = 0.5
        else:
            P[0][index] = 1

    for index_i in range(1, i):
        for index_j in range(1, j):
            P[index_i][index_j] = 0.5 * (P[index_i - 1][index_j] + P[index_i][index_j - 1])

    return P

print(funkcja_P(5, 4))

    