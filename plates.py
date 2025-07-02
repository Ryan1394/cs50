# wrong code

# def main2():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid2(s):
#     if len(s) > 6 or len(s) < 2:
#         return False
#     if not (s[0].isalpha() or s[1].isalpha()):
#         return False
#     for i in s:
#         if i == "0" and s[s.index[i-1]].isalpha():
#             return False
#         elif i.isdigit() and not s[s.index(i):].isdigit():
#                 return False
#         elif not i.isalnum():
#                 return False
#         else:
#             return True


# main()
########
# correct code

def main():
    while True:
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: All characters must be alphanumeric
    if not s.isalnum():
        return False

    # Rule 4: Digits cannot start with '0' and must be at the end
    digit_found = False
    for char in s:
        if char.isdigit():
            if not digit_found and char == '0':  # First digit is '0' → invalid
                return False
            digit_found = True
        elif digit_found:  # Letter appears after digit → invalid
            return False

    return True


if __name__ == "__main__":
    main()