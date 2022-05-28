n = int(input())
control_word = input()
string = []

for i in range(n):
    current_string = input()
    string.append(current_string)
print(string)
for i in range(len(string) - 1, -1, -1):
    element = string[i]
    if control_word not in element:
        string.remove(element)
print(string)