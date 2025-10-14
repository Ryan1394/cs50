def main():
    plate = input("Plate : ")
    if its_valid(plate):
        print("valid")
    else:
        print("invalid")

def its_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not (s[0].isalpha() or s[1].isalpha()):
        return False
    else:
        for i in s:
            if i =="0" and s[s.index(i)-1].isalpha():
                return False
            elif i.isdigit() and not s[s.index(i):].isdigit():
                return False
            elif not i.isalnum():
                return False
        return True
    

if __name__ == "__main__":
    main()