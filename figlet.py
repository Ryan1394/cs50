# - - - - - LIBRARIES - - - - -
from pyfiglet import Figlet
import random
import sys
# - - - - - LIBRARIES - - - - -

figlet = Figlet()

# - - - - - font(s) - - - - -
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(font_list)

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in font_list:
            font = sys.argv[2]
        else:
            sys.exit('Invalid command-line argument')
    else:
        sys.exit("provide -f or --font as second command-line argument")

if len(sys.argv) == 2:
    sys.exit("Too many command-line argument")

s = input("type : ")
f = figlet.setFont(font=font)                                                                                                           # type: ignore
print(figlet.renderText(s)) 