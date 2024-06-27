import sys

N = int(sys.stdin.readline())

tmp = 9999
rs = 9999
num = int(N / 5) if N / 5 else 0

# 5로만 빼는 경우
if (N % 5) == 0:
    tmp = N / 5

    if tmp < rs:
        rs = tmp

# 3으로만 빼는 경우
if (N % 3) == 0:
    tmp = N / 3

    if tmp < rs:
        rs = tmp

# 5로 뺄셈이 가능한 경우
if num > 0:
    # 5로 뺄셈하는 비중을 늘림
    for n in range(1, num + 1):
        if N - (n * 5) >= 0:
            mod = N - (n * 5)
            # 3을 빼본다
            if (mod % 3) == 0:
                tmp = (mod / 3) + n

                if tmp < rs:
                    rs = tmp

# rs가 어떤 값으로도 갱신되지 못했다
if rs == 9999:
    # 뺄셈 불가
    rs = -1

print(int(rs))