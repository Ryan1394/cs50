def main():
    inp: str = input("Input : ")
    print(shorten(inp))

def shorten(word : str):
    for l in word:
        if l.lower() in ["a","e","i","o","u"]:
            word = word.replace(l,"")
    return word

if __name__ == "__main__":
    main()