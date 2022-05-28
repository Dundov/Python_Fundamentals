word_1 = input()
word_2 = input()

unique_word = ""
first_print = word_1

for index in range(len(word_1)):
    for y in range(index + 1):
        unique_word += word_2[y]
    for z in range(index + 1, len(word_2)):
        unique_word += word_1[z]
    if not unique_word == first_print:
        print(unique_word)
    first_print = unique_word
    unique_word = ""

