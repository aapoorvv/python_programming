alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text,shift):  
    new = ""
    for i in text:
        if shift<0:
            c = alphabet.index(i)-((-shift)%26)
        else:
            c = alphabet.index(i)+(shift%26)
            if c>25:
                c = c%26
        new = new + alphabet[c]  
    print(f"The encoded text is {new}.")

def decode(text,shift):
    new = ""
    for i in text:
        if shift<0:
            c = alphabet.index(i)+((-shift)%26)
            if c>25:
                c = c%26
        else:
            c = alphabet.index(i)-(shift%26)    
        new = new + alphabet[c]  
    print(f"The decoded text is {new}.")
print('''🄲 🄸 🄿 🄷 🄴 🅁''')   
while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:  ").lower()
    shift = int(input("Type the shift number:  "))

    if direction=="encode":
        encode(text,shift)
    else: 
        decode(text,shift)
    user = input("Do you want to continue? yes or no:  ")
    if(user=="no"):
        print("Goodbye.")
        break;
