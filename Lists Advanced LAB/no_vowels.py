text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
res = [c for c in text if c not in vowels]
res_as_text = "".join(res)
print(res_as_text)