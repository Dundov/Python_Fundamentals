name = ""
command = ""

while command != "Welkome!":
    name = input()
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(name) < 5 and name != "Welcome!":
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5 and name != "Welcome!":
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6 and name != "Welcome!":
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6 and name != "Welcome!":
        print(f"{name} goes to Hufflepuff.")

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break