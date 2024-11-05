def hanoi(disks, first, second, third, moves):
    if disks == 1:
        moves.append(f'передвинуть диск с {first} на {third}')
    else:
        hanoi(disks - 1, first, third, second, moves)  # Move n-1 disks from first to second
        moves.append(f'передвинуть диск с {first} на {third}')  # Move the nth disk from first to third
        hanoi(disks - 1, second, first, third, moves)  # Move n-1 disks from second to third
# Input number of disks
disks = int(input("Введите количество дисков: "))
first = 'A'  # Name of the first peg
second = 'B'  # Name of the second peg
third = 'C'   # Name of the third peg
moves = []
# Call the hanoi function
hanoi(disks, first, second, third, moves)
# Print the moves
for move in moves:
    print(move)