from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        birthday = input("date of birth : ")
        y,m,d = birthday.split('-')
        age = convert(y,m,d)
        print(num2word(age),'minutes')
    except:
        sys.exit("Invalid date")

def convert(y,m,d):
    try:
        t_day = date.today()
        b_day = date(int(y),int(m),int(d))
        age = t_day - b_day
    except:
        sys.exit("Invalid date")
    return age.days * 1440

def num2word(num):
    word = p.number_to_words(num,andword='').capitalize()
    return word


if __name__ == "__main__":
    main()