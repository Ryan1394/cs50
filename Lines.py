import sys
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
else:
    try:
        with open(sys.argv[1]) as f:
            counter = 0
            for i in f:
                if i.lstrip().startswith("#"):
                    continue
                elif i.lstrip() == " ":
                    continue
                else:
                    counter += 1
            print(counter)
    except FileNotFoundError:
        sys.exit("File Does Not Exists")