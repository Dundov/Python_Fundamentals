divisor = int(input())
boundary = int(input())
for i in range(1, boundary + 1):
    if boundary % divisor == 0:
        print(f"{boundary}")
        break
    else:
        boundary -= 1