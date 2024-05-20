import sys

E, S, M = map(int, sys.stdin.readline().split())

ESM = str(E) + " " + str(S) + " " + str(M)

E_MAX = 15
S_MAX = 28
M_MAX = 19

E_TMP = 0
S_TMP = 0
M_TMP = 0

Y = 0

while (str(E_TMP) + " " + str(S_TMP) + " " + str(M_TMP)) != ESM:
    if E_TMP == E_MAX:
        E_TMP = 1
    else:
        E_TMP += 1

    if S_TMP == S_MAX:
        S_TMP = 1
    else:
        S_TMP += 1

    if M_TMP == M_MAX:
        M_TMP = 1
    else:
        M_TMP += 1

    Y += 1

print(Y)
