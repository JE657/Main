

champs = []
while True:
    print("Enter a champion: ")
    x = input()
    if x == 'b':
        break
    else:
        champs.append(x)

for i in range(len(champs)):
    if i+1 < len(champs)-1:
        if champs[i] < champs[i+1]:
            print(f'{champs[i]} is less than {champs[i+1]}')

print(*champs)

