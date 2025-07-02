import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name : ")
        name_list.append(name)
    except EOFError:
        print()
        break
output = p.join(name_list)
print(f"Adieu, Adieu, to { output }")