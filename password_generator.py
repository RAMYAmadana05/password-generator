import random 
import string

print("Enter the desired length for the generated password\n(Preferred: 8-16 characters)")
length=int(input("Length: "))

def generation():

    print("Enter the desired choice (1.Only Numbers/ 2. Only Letters/ 3. Anything)")
    pattern=int(input("Pattern: "))

    password=""

    if pattern==1:
        for i in range(length):
            password += str(random.choice("0123456789"))

    elif pattern==2:
        for i in range(length):
            password += str(random.choice(string.ascii_letters))
    
    elif pattern==3:
        for i in range(length):
            password += str(chr(random.choice([random.randint(65,90),random.randint(97,122),random.randint(33,47),random.randint(58,64),random.randint(91,96)])))
    
    else:
        print("invalid choice!")

    print("The generated password is:", password)

if length<6:
    print("NOTE: password length is too small!")

elif length>16:
    print("NOTE: password length is too big!")

else:
    generation()