def main():
    while True:
        try:
            fraction = input("Fraction : ")
            p = convert(fraction)
            x = gauge(p)
            print(x)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    p = (int(x)/int(y))*100
    return p

def gauge(percentage):
    if percentage <= 1:
        x = "E"
    elif percentage >= 99:
        x = "F"
    else:
        a = int(percentage)
        x = str(a)+"%"
    return x

if __name__ == "__main__":
    main()