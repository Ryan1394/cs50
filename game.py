import random
while True: 
    try:
        n = int(input("LeveL : "))
        if n > 0:
            number = random.randint(0,n)
    except ValueError:
        continue
    else:
        break
while True:
    try:
        guess = int(input("guess: "))
    except ValueError:
        continue
    if guess < number:
        print("Too Small!")
        continue
    if guess > number:
        print("Too Large!")
        continue
    else:
        print("Just Right ;)")
        break