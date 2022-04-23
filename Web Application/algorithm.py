import numpy as np


def needleman_wunsch(s1, s2):
    l1, l2 = len(s1), len(s2)
    E = np.zeros((l1 + 1, l2 + 1), dtype=int)  # edit distance
    P = np.zeros((l1 + 1, l2 + 1), dtype=int)  # previous
    for i in range(l1 + 1):
        E[i][0] = i
        P[i][0] = 1
    for j in range(l2 + 1):
        E[0][j] = j
        P[0][j] = 2

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            m = min(E[i - 1][j] + 1, E[i][j - 1] + 1, E[i - 1][j - 1] + (1 - (s1[i - 1] == s2[j - 1])))
            if m == E[i - 1][j] + 1:
                E[i][j] = E[i - 1][j] + 1
                P[i][j] = 1

            elif m == E[i][j - 1] + 1:
                E[i][j] = E[i][j - 1] + 1
                P[i][j] = 2

            else:
                E[i][j] = E[i - 1][j - 1] + (1 - (s1[i - 1] == s2[j - 1]))
                P[i][j] = 3

    n1, n2 = '', ''
    i, j = l1, l2
    while (i > 0) or (j > 0):
        if P[i][j] == 1:
            i -= 1
            n1 += s1[i]
            n2 += '-'
        elif P[i][j] == 2:
            j -= 1
            n1 += '-'
            n2 += s2[j]
        else:
            n1 += s1[i - 1]
            n2 += s2[j - 1]
            i, j = i - 1, j - 1

    n1, n2 = n1[::-1], n2[::-1]

    return E[l1, l2], (n1, n2)
