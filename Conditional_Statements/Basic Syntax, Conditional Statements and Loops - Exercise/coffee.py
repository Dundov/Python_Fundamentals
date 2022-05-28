number_of_cofee = 0
command = ""
while command.lower() != ("end"):
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" \
            or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            number_of_cofee += 1
        else:
            number_of_cofee += 2
if number_of_cofee > 5:
    print("You need extra sleep")
else:
    print(number_of_cofee)

