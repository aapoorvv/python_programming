marks = [95, 33, 55, "Maths"]
print(marks[0])
print(marks[3])
print(marks[-3])
print(marks[0:2])

for score in marks:
    print(score)
marks[0]=94
marks.append(69)
print(marks)

marks.insert(3,20)
print(marks)

print(20 in marks)

print(len(marks))

marks.clear()
print(marks)