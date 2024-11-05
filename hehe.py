def hanoi(disks, first, second, third, moves):
    if disks == 1:
        moves.append(f'передвинуть диск со стрержня {first} на {third}')
    else:
        hanoi(disks - 1, first, third, second, moves)
        moves.append(f'передвинуть диск со стрержня {first} на {third}')
        hanoi(disks - 1, second, first, third, moves)
disks = int(input("Введите количество дисков: "))
first = 'A'
second = 'B'
third = 'C'
moves = []
hanoi(disks, first, second, third, moves)
for move in moves:
    print(move)
with open('решение.txt', 'w', encoding='utf-8') as file:
    file.writelines(moves)
