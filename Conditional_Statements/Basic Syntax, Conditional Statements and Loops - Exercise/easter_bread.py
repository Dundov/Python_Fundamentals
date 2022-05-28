budget = float(input())
price_for_kg_flour = float(input())

price_of_flour_in_bread = price_for_kg_flour
price_of_eggs_in_bread = price_for_kg_flour * 0.75
price_of_milk_in_bread = (price_of_flour_in_bread * 1.25) / 4
easter_bread_price = price_of_flour_in_bread + price_of_eggs_in_bread + price_of_milk_in_bread
easter_bread_counter = 0
colored_eggs = 0

while budget >= easter_bread_price:
    easter_bread_counter += 1
    budget -= easter_bread_price
    colored_eggs += 3
    if easter_bread_counter % 3 == 0:
        colored_eggs -= (easter_bread_counter - 2)
print(f"You made {easter_bread_counter} loaves of Easter bread! Now you have " 
      f"{colored_eggs} eggs and {budget:.2f}BGN left.")