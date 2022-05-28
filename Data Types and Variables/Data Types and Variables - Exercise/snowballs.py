from math import pow

number_of_snowballs = int(input())
max_value = 0
max_snowballs_weight = 0
max_snowballs_time = 0
max_snowballs_quality = 0

for snowball in range(number_of_snowballs):
    snowballs_weight = int(input())
    snowballs_time = int(input())
    snowballs_quality = int(input())
    current_snowball_value = pow(snowballs_weight / snowballs_time, snowballs_quality)
    if current_snowball_value > max_value:
        max_value = current_snowball_value
        max_snowballs_weight = snowballs_weight
        max_snowballs_time = snowballs_time
        max_snowballs_quality = snowballs_quality
print(f"{max_snowballs_weight} : {max_snowballs_time} = {int(max_value)} ({max_snowballs_quality})")