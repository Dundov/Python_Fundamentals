n = int(input())
wagons = [0] * n
command_input = input()
while command_input != "End":
    command_arg = command_input.split(" ")
    command = command_arg[0]
    first_num = int(command_arg[1])

    if command == "add":
        wagons[-1] += first_num
    elif command == "insert":
        second_num = int(command_arg[2])
        wagons[first_num] += second_num
    elif command == "leave":
        second_num = int(command_arg[2])
        wagons[first_num] -= second_num
    command_input = input()
print(wagons)