# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(raw_input())
fac = 1

for i in range(1, user_input + 1):
	fac *= i

print(str(fac % 1000000007))