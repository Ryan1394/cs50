import random

# --------- { level part } ---------
while True:
    n = int(input("level : "))
    try:
        if n > 0:
            number = random.randint(1,n)
    except ValueError:
        continue
    else:
        break

# --------- { Guess Part } ---------
while True:
    try:
        user_input = int(input("Guess : "))
    except ValueError:
        continue
    if user_input < number: # type: ignore
        print("too small !!!")
        continue
    if user_input > number: # type: ignore
        print("too large !!!")
        continue
    else:
        print("just right.")
        break