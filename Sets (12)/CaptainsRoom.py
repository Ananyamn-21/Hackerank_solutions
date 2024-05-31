# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# # You only know the value of  and the room number list.
K = int(input())
rooms = list(map(int,input().split()))
checked = set()
repeated = set()
for i in rooms:
    if i in checked:
        repeated.add(i)
    else:
        checked.add(i)
print(sum(checked-repeated))