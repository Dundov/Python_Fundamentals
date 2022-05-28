def is_perfect(some_number):
    sum = 0
    for devisor in range(1, some_number):
        if some_number % devisor == 0:
            sum += devisor
    if sum == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect(number))
