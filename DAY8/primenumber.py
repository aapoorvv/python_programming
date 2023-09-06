def prime(n):
    flag = True;
    for i in range(2,n//2+1):
        if n%i==0:
            flag = False
            break
    if flag :
        print("It is a Prime no.")
    else:
        print("It is not a Prime no.")

n = int(input("Enter a positive no.: "))
prime(n)