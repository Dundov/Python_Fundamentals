string = input()
lower_case_string = string.lower()
word = 0

for c in lower_case_string:
    if "sand" in lower_case_string:
        word += 1
    elif "sun" in lower_case_string:
        word += 1
    elif "fish" in lower_case_string:
        word += 1
    elif "water" in lower_case_string:
        word += 1

print(word)
