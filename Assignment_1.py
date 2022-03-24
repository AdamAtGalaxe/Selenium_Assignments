from math import pi

#1.  Write a Python program which accepts the radius of a circle from the user and compute the area.
def radius():
    while True:
        try:
            rad = float(input("Input the radius of the circle : "))
            break
        except:
            print("That is not a valid number")
            continue
    print("The are is %.2f" %(pi*rad**2))
#2. Write a Python program which accepts the user's first and last name and print them.
def name():
    while True:
        try:
            first = input("Input your first name: ")
            last = input("Input your last name: ")
            if first.isnumeric() or last.isnumeric():
                raise
            break
        except:
            print("That is not a valid name")
            continue
    print("Welcome {} {}.".format(first, last))
#3. Write a Python program to display the first and last colors from the following list. color_list = ["Red","Green","White" ,"Black"]
def colors():
    color_list = ["Red","Green","White" ,"Black"]
    print("Your first color is {} and your last is {}".format(color_list[0], color_list[len(color_list)-1]))

#4. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def exponentialGrowth():
    while True:
        try:
            num = int(input("Input a number: "))
            break
        except:
            print("That is not a valid number")
            continue
    print("Your total is {}".format(num+(num**2)+(num**3)))
#5. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 then multiply it by 20.
def difference():
    while True:
        try:
            num = int(input("Input a number: "))
            break
        except:
            print("That is not a valid number")
            continue
    if(num>17):
        num -= 17
    elif(num<17):
        num = 17-num
    else:
        num*=20

    print(num)
#6. Write a Python program to test whether a number is within 100 of 1000 or 2000.
def range():
    while True:
        try:
            num = int(input("Input a number: "))
            break
        except:
            print("That is not a valid number")
            continue
    if (num > 899 and num < 1101) or (num > 1899 and num < 2101):
        print("yes")
    else:
        print("no")
def counter():
    i = 1
    while(i<101):
        print(i)
        i += 1

#radius()
#name()
#colors()
#exponentialGrowth()
#difference()
#range()
counter()
