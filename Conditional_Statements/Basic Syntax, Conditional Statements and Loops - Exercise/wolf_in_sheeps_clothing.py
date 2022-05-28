string = input().split(", ")
rev_string = string[::-1]

wolf_index = 0
n = 0
for i in range(len(rev_string)):
    wolf_index = rev_string.index("wolf") + 1

if wolf_index == 1:
    print("Please go away and stop eating my sheep")
else:
    n = wolf_index - 1
    print(f"Oi! Sheep number {n}! You are about to be eaten by a wolf!")

