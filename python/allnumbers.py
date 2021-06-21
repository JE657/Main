# HackerRank Challenge (?)

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

allnumbers = True
hasnumbers = False

user_input = input("Enter a sentence ")

for i in user_input:
    if i in numbers:
        hasnumbers = True
        print("Contains a", i)
    else:
        allnumbers = False

print("Has Numbers", hasnumbers)
print("All Numbers", allnumbers)

