import random


def main():
    score = 0
    counter = 0
    level = get_level()
    while counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(f"{x} + {y} = ")
        if answer == str(x+y):
            score += 1
            counter += 1
        elif answer != str(x+y):
            counter_2 = 0
            while counter_2 < 2:
                print("EEE")
                answer = input(f"{x} + {y} = ")
                counter_2 += 1
            print(f"{x} + {y} = {int(x)+int(y)}") 
    print(f"your score is {score}")

def get_level():
    while True:
        try:
            level = (int(input("Level : ")))
            if level not in [1,2,3]:
                continue
            else:
                break
        except:
            continue
    return level


def generate_integer(level):
    if level == 1:
        level = random.randint(0,9)
    if level == 2:
        level = random.randint(10,19)
    if level == 3:
        level = random.randint(100,999)
    return level


if __name__ == "__main__":
    main()