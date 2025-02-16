import random
print("Guess the number game")
v = int(input("How many attempt you want? "))
i = int(input("How many range of number you want to guess "))
x = random.randint(1,i)
z = 0
while z < 99:
    z = z+1 
    y = int(input("Enter your guess "))
    if y == x:
        print("You won")
        print("You guessed it at", z, "try")
        stat = 1
        break
    elif z == v:
        print("Sorry you ran out of attempt")
        print("The answer is", x)
        stat = 0
        break
    else:
        print("Nope try again")
        if y > x:
            w = "high"
        else:
            w = "low"
        print("You guessed to", w)
if stat == 1:
    print("Congrats btw, see you later")
else:
    print("Aww, dont cry, see you again")