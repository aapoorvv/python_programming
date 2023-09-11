s = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 52,
}

for i in s:
    if 100 >= s[i] >90:
        s[i] = "Outstading"
    elif 90>= s[i] > 80:
        s[i] = "Exceeds expectation"
    elif 80>= s[i] >60:
        s[i] = "Acceptable"
    elif 60>= s[i] >=50:
        s[i] = "Need to improve"
    else:
        i = "FAIL"
print(s)