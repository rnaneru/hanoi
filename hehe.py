def hanoi(disks, first, second, third):
    if disks == 1:
        moves.append ('передвинуть диск с {first} на {third}')

disks = int(input())
first = []
second = []
third = []
moves = []
for i in range (disks):
    first.append (i)
    hanoi(disks, first, second, third)
print (moves)