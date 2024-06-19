

#Write a program that takes two numbers as input and prints their sum.
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
sum = float(num1) + float(num2)
print("the sum of num1{0} and num2 {1} is sum{2}", sum)


#Write a python program that checks whether a given number is even or odd
num1 = int(input("enter the number:"))
if(num1 % 2) == 0:
  print( "num1 {0} is even")
else:
  print ("num1 {0} is odd")


#Write a python program that calculates the factorial of a given number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
num = 5
print("Factorial of",num,"is",factorial(num))


#Write a program that asks the user for their name and then prints a greeting message.
name = input("Enter your name")
print(name, "Have a good day!")


#Write a program that takes a string input from the user and writes it to a text file.
#Write a program that reads the content of a text file and prints it to the console.


#Write a python program that takes a string as input and returns its length.
str = input("enter the string:")
print("Length of the string is:", len(str))

#Write a python program that concatenates two strings and returns the result.
var1 = input("Enter first input:")
var2 = input("Enter second input:")
var3 = var1 + var2 
print(var3)


#Write a python program that checks if a substring is present in a given string.
str1 = "India Gate is in NewDelhi"
if "Gate" in str1:
    print("Yes it is present in the string.")
else:
    print("NOt present in the string. ")



#Write a python program that converts a given string to uppercase.
str1 = input("Enter a sentence:")
print(str1.upper())


#Write a python program that generates the first n numbers in the fibonacci sequence.

#Write a python program that calculates the sum of the digits of a given number.
num = input("Enter a number")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)


#Write a program that asks the user for their birth year and calculates their age.
#Write a program that reads data from a CSV file and prints it to the console.

#Write a program in python that counts the frequency of each character in a string.
from collections import Counter
test_str = "Parnitha Reddy"
res = Counter(test_str)
print("count all the characters in Parnitha reddy:/n" + str(res))



#Write a program in python that converts a given string to title case (first letter of each word capitalized)
test_str = ("indira gandhi delhi technical university")
print("The original string is: " + str(test_str))
res = test_str.capitalize()
print("The string after uppercasting initial character:" + str(res))


#Write a python program that checks if two strings are anagrams of each other.

def check (s1,s2):
if (sorted(s1) == sorted(s2))
     print("that the strings are anagrams.")
else:
    print("that the strings arent anagrams.")
s1 = input("Enter the first input:")
s2 = input("Enter the second input:")
check(s1, s2)


#Write a python program that removes all punctuation from a given string.
import string
test_str = "PaRi, is the best: for ! EGO:"
print("The original string is:" + test_str)
for punctuation in string.punctuation:
     test_str = test_str.replace(punctuation, '')
print(" The string after punctuation filter : " + test_str)


#Write a python program that takes a list of numbers and returns their sum.
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list:" , total)


#Write a python program that counts the occurrences of a specific element in a list.
from collections import Counter
1 = [1,1,1,2,3,4,5,6,7,1,]
x = 1
d = Counter(1)
print("{}has occurred {}times".format(x,d[x]))


#Write a python program that returns the minimum and maximum values in a list of numbers.
list=[34,64,23,99, 12,9]
list.sort()
print(list)


#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
celsius = 50
fahrenheit = (celsius * 1.8) + 32
print('%.2f Celsius is equivalent to: %.2f Fahrenheit' % (celsius, fahrenheit))


#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def add(num1, num2):
     return num1 + num2 
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2 

print("Please select opertion -\n" \
      "1. Add\n" \
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Divide\n")
      

select = int(input("Select operations form 1,2,3,4:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number:"))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

          
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "-", number_2, "=", multiply(number_1,Numner_2))

elif select == 4:
    print(number_1, "/", number_2,"=", divide(number_1, number_2))

else:
    print("Invaild input")


#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
#Write a program that copies the contents of one text file to another.


#Write a program in python that converts a string into a list of its characters.
def Convert(string): 
	li = list(string.split(" ")) 
	return li 
str1 = "Geeks for Geeks"
print(Convert(str1)) 





          





