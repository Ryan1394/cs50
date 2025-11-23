import sys
from PIL import Image,ImageOps

try:
    if len(sys.argv) < 3:
        sys.exit("Too Few Command-Line Arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too Many Command-Line Arguments")
    elif not(sys.argv[1] or sys.argv[2]).endswith(".jpg" or ".jpeg" or ".png"):
        sys.exit("Invalid Output")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input And Output Have Different Extensions")
    else:
        img = Image.open(sys.argv[1])
        img2 =  Image.open("shirt.png")
        size = img2.size
        muppet = ImageOps.fit(img,size)
        muppet.paste(img2,img2)
        muppet.save(sys.argv[2])
        
except FileNotFoundError:
    sys.exit("File Does Not Exist")