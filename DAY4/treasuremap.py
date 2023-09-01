row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
a = position//10 #or a=position[0]
b = position%10  #or b=position[1]

map[a-1][b-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")