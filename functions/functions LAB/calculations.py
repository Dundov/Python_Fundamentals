def calculate(a, b, operator):
    result = None
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    return result


operator = input()
a = int(input())
b = int(input())
result = calculate(a, b, operator)
print(result)
