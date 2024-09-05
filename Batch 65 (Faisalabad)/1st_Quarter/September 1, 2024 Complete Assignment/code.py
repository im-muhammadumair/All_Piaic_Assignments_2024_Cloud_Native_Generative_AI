# Even or Odd.

num = int(input("Enter num: "))
if num%2 == 0:
    print(f"The number {num} is Even!")
else:
    print(f"The number {num} is Odd!")

#Positive, Negative, or Zero.

num = int(input("Enter num: "))
if num<0:
    print("The number is less than zero!")
if num>0:
    print("The number is greater than zero!")
if num==0:
    print("The number is zero!")

# Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.

num = int(input("Enter num: "))
if num%2 == 0 and num%3 == 0:
    if num%2 ==0:
        print("The number is divisible by 2")
    elif num%2 ==0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 2 and 3")


# - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."

age = int(input("Enter the age: "))
nationality = (input("Enter your nationality: ")).lower()
if age >= 18:
    if nationality == "pakistani":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")

# Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)

age = int(input("Enter the age: "))
if 0< age <= 12:
    print("You are a child")
elif 13< age >= 19:
    print("You are a teenager!")
elif 20< age >= 59:
    print("You are a adult!")
elif 59< age >= 60:
    print("You are a Senior citizen!")
elif age<0:
    print("You are a Senior citizen!")
elif age<98:
    print("You are a dead man 😂!")

else:
    print("Wrong age")


#  - Enter a month (as a number between 1 and 12). Print the number of days in that month.
month_number = int(input("Enter the month number: "))

if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")

elif month_number <=0:
    print("Month number cant be Negative!")
else:
    print("Only 12 months Exists!")

#                                     or 

month_number = int(input("Enter the month number: "))
match month_number:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Only 12 months exists!")
        


# Assume a non-leap year.
#  - Check if a year is a leap year or not.

year = int(input("Enter the year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Yes, {year} is a leap year")
else:
    print(f"The {year} is Not a Leap Year")