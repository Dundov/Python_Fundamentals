sentence = ""
while sentence != "End":
    sentence = input()
    if sentence == "SoftUni" or sentence == "End":
        continue
    for letter in (sentence):
        print(letter * 2, end="")
    print()