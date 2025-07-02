def main():
    x = input("What time is it ? ")
    if 7 <= convert(x) <= 8:
        print("it's breakfast time")
    elif 15 <= convert(x) <= 18:
        print("it's lunch time")
    elif 19 <= convert(x) <= 22:
        print("it's dinner time")
    else:
        print("")
def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y) / 60
    return x + y

if __name__ == "__main__":
    main()