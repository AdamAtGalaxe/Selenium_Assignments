#1.Create a function, Assign a different name to function and call it through the new name.
import inspect

def myName():
    caller_name = inspect.currentframe().f_code.co_name
    print("My called method name is", caller_name)

#test = myName()
#test

#2. print the string in reverse order
def reverse(word: str):
    return word[::-1]

#print(reverse("test"))

#3. find all even number from  1 - 100.
def evens():
    for num in range(2, 101, 2):
        #if num%2 == 0 :
        print(num)

#evens()

#4. Generate a Python list of all the even numbers between 4 to 30
def evenArray():
    temp = []
    for num in range(4, 31, 2):
        temp.append(num)
    return temp

#print(evenArray())

#5. Find the largest item from a given list(Hint, Use MAX function)
def largest(myArray: []):
    return max(myArray)

#print(largest([1,2,6,4,7,8,9]))
#6. Print the following pattern 1 1 2 1 2 3 1 2 3 4 1 2 3 4 5
def increment():
    for i in range(1, 6):
        for k in range(1, i+1):
            print("{} ".format(k), end="")

        print()

#increment()
#7. Calculate the sum of all numbers from  1 to a given number
def sum(top: int):
    temp = 0
    for i in range(1, top+1):
        temp += i
    return temp

#print(sum(5))

#8. Print list in reverse order using a loop list1 = [10, 20, 30, 40, 50]
def reverseArray(myArray: []):
    tempArray = myArray
    for i in range(0,int(len(myArray)/2)):
        temp = myArray[i]
        myArray[i] = myArray[len(myArray)-i-1]
        myArray[len(myArray) - i - 1] = temp
    print(myArray)

#reverseArray([10, 20, 30, 40, 50])
#9. Display numbers from  -10 to - 1 using for loop
def negatives():
    for i in range(-10, 0):
        print(i)
#negatives()
#10.Write program to display all prime numbers within a range
def primes(top: int):
    for num in range(2, top):
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
#primes(20)



