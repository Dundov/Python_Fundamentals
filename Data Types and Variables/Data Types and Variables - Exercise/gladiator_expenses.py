number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_of_helmet_broken = number_of_lost_fights // 2
total_of_sword_broken = number_of_lost_fights // 3
total_of_shield_broken = number_of_lost_fights // 6
total_of_armor_broken = total_of_shield_broken // 2

expenses = total_of_helmet_broken * helmet_price + total_of_sword_broken * sword_price \
           + total_of_shield_broken * shield_price + total_of_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")