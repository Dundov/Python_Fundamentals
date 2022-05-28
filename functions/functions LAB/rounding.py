args = input().split(" ")
numbers = []

for arg in args:
    num = float(arg)
    round_num = round(num)
    numbers.append(round_num)
print(numbers)