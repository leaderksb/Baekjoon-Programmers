import sys

N, M = map(int, sys.stdin.readline().split())
ori_arr = [[''] * M for _ in range(0, N)]
new_line = ''
new_arr = []

black_arr = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

white_arr = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

X = 0
Y = 0
min_cnt = 64


def diff():
    black_cnt = 0
    white_cnt = 0

    for n in range(0, 8):
        for m in range(0, 8):
            if black_arr[n][m] != new_arr[n][m]:
                black_cnt += 1
            if white_arr[n][m] != new_arr[n][m]:
                white_cnt += 1

    if black_cnt < white_cnt:
        return black_cnt
    else:
        return white_cnt


for n in range(0, N):
    ori_line = list(str(sys.stdin.readline().strip()))
    ori_arr[n] = ori_line

while True:
    for x in range(X, X + 8):
        for y in range(Y, Y + 8):
            new_line += ori_arr[x][y]
        new_arr.append(list(new_line.strip()))
        new_line = ''
    diff_cnt = diff()

    if min_cnt > diff_cnt:
        min_cnt = diff_cnt

    new_arr.clear()

    if X + 8 < N:
        X += 1
    else:
        if Y + 8 < M:
            X = 0
            Y += 1
        else:
            print(min_cnt)
            break
