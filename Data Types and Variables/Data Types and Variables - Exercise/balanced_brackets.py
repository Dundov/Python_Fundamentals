number_of_strings = int(input())
open_string = 0
closed_string = 0
for char in range(1, number_of_strings + 1):
    string = input()
    if string == '(' or string == '( ' or string == ' (':
        open_string += 1
    if string == ')' or string == ') ' or string == ' )':
        closed_string += 1
if open_string == closed_string:
    print("BALANCED")
else:
    print("UNBALANCED")

# lines = int(input())
#
# is_balanced = True
# has_open_bracket = False
#
# for _ in range(0, lines):
#     line = input()
#     if line != '(' and line != ')':
#         continue
#
#     is_open_bracket = line == '('
#     if has_open_bracket == is_open_bracket:
#         is_balanced = False
#         break
#
#     has_open_bracket = is_open_bracket
#
# if is_balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')

