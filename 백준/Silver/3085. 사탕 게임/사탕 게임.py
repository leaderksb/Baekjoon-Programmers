import sys

N = int(sys.stdin.readline())

all_arr = []
line_arr = []
candy_max = 1

# 사탕판 2차원 배열로 입력받기
for i in range(0, N):
    line = str(sys.stdin.readline())
    for j in range(0, N):
        line_arr.append(line[j])
    all_arr.append(line_arr.copy())
    line_arr.clear()

# 사탕의 최대 개수 비교
def diff(cnt):
    global candy_max

    if candy_max < cnt:
        candy_max = cnt

def candy_x(fix):  # x축 고정
    global candy_max

    cnt = 1  # msg의 연속 개수
    num = 0  # 현재 확인하고 있는 인덱스 위치
    msg = all_arr[fix][0]  # 비교할 문자열

    while num + 1 < N:
        if msg == all_arr[fix][num + 1]:
            cnt += 1
            diff(cnt)
        else:
            diff(cnt)
            msg = all_arr[fix][num + 1]
            cnt = 1
        num += 1


def candy_y(fix):  # y축 고정
    global candy_max

    cnt = 1  # msg의 연속 개수
    num = 0  # 현재 확인하고 있는 인덱스 위치
    msg = all_arr[0][fix]  # 비교할 문자열

    while num + 1 < N:
        if msg == all_arr[num + 1][fix]:
            cnt += 1
            diff(cnt)
        else:
            diff(cnt)
            msg = all_arr[num + 1][fix]
            cnt = 1
        num += 1


# 초기 사탕판의 최대 개수 구하기
for n in range(0, N):
    candy_x(n)
    candy_y(n)

# 현재 바꾸려는 인덱스 위치
spot = 0

while spot + 1 < N:  # x축 고정

    for n in range(0, N):

        # new_arr = list(all_arr)
        before_spot = all_arr[n][spot]
        after_spot = all_arr[n][spot + 1]

        all_arr[n][spot] = after_spot
        all_arr[n][spot + 1] = before_spot

        candy_x(n)
        candy_y(spot)
        candy_y(spot + 1)

        before_spot = all_arr[n][spot]
        after_spot = all_arr[n][spot + 1]

        all_arr[n][spot] = after_spot
        all_arr[n][spot + 1] = before_spot

    spot += 1

# 현재 바꾸려는 인덱스 위치
spot = 0

while spot + 1 < N:  # y축 고정

    for n in range(0, N):

        # new_arr = list(all_arr)
        before_spot = all_arr[spot][n]
        after_spot = all_arr[spot + 1][n]

        all_arr[spot][n] = after_spot
        all_arr[spot + 1][n] = before_spot

        candy_y(n)
        candy_x(spot)
        candy_x(spot + 1)

        before_spot = all_arr[spot][n]
        after_spot = all_arr[spot + 1][n]

        all_arr[spot][n] = after_spot
        all_arr[spot + 1][n] = before_spot

    spot += 1

print(candy_max)