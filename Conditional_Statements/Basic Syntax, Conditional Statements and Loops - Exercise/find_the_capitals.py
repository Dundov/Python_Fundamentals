string = input()
list_of_capital_letters = []
for c in range(len(string)):
    if string[c].isupper():
        list_of_capital_letters.append(c)
print(list_of_capital_letters, end="")

