import random
import string
def main():
    length=int(input("Enter length of password \n"))
    low=string.ascii_lowercase
    up=string.ascii_uppercase
    num=string.digits
    spchar=string.punctuation
    add=low+up+num+spchar
    x=random.sample(add,length)
    password="".join(x)
    print(password)
    main()
main()  