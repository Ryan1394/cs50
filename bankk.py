def main():
    x = input("greeting : ").strip()
    print("$"+str(value(x)))

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 25
    else:
        return 100
    
if __name__ =="__main__":
    main()