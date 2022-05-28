tank_capacity = 255
number_of_lines = int(input())
total_debit = 0

for i in range(number_of_lines):
    litters = int(input())
    total_debit += litters
    if total_debit > tank_capacity:
        print("Insufficient capacity!")
        total_debit -= litters
print(f"{total_debit}")