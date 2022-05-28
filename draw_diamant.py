from math import floor
from math import ceil

number = int(input())

for i in range(0, ceil(number / 2)):
    leftright = floor((number - 1) / 2) - i
    mid = number - 2 * leftright - 2
    if mid >= 0:
        print("-" * leftright + "*" + "-" * mid + "*" + "-" * leftright)
    else:
        print("-" * leftright + "*" + "-" * leftright)
for i in range(ceil((number - 4) / 2), -1, -1):
    leftright = floor((number - 1) / 2) - i
    mid = number - 2 * leftright - 2
    if mid >= 0:
        print("-" * leftright + "*" + "-" * mid + "*" + "-" * leftright)
    else:
        print("-" * leftright + "*" + "-" * leftright)