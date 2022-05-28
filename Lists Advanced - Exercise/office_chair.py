# number_of_rooms = int(input())
# total_free_chairs = 0
# for n in range(1, number_of_rooms + 1):
#     number = input().split()
#     chairs = int(len(number[0]))
#     visitors = int(number[1])
#     free_chairs = chairs - visitors
#     total_free_chairs += free_chairs
#     if visitors > chairs:
#         needed_chairs = visitors - chairs
#         print(f"{needed_chairs} more chairs needed in room {n}")
#     elif visitors <= total_free_chairs:
#         free_chairs = chairs - visitors
#         total_free_chairs += free_chairs
#         print(f"Game On, {total_free_chairs} free chairs left")
n = int(input())

count_free_seats = 0
needed_chairs = 0
number_of_room = 1

for i in range(0, n):
    chairs, people = input().split()

    if len(chairs) > int(people):
        free_seats = len(chairs) - int(people)
        count_free_seats += free_seats
    elif len(chairs) < int(people):
        needed_chairs = abs(len(chairs) - int(people))
        count_free_seats -= needed_chairs
        print(f"{needed_chairs} more chairs needed in room {number_of_room}")

    number_of_room += 1

if count_free_seats >= 0:
    print(f"Game On, {count_free_seats} free chairs left")