key = int(input())
number_of_lines = int(input())
decrypted_letter = ""
for number in range (1, number_of_lines + 1):
    letter = input()
    decrypted_letter += chr(ord(letter) + key)

print(decrypted_letter)