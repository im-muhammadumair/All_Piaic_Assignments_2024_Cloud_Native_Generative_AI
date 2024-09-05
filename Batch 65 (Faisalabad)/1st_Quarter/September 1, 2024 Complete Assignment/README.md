# PIAIC ASSIGNMENT-Batch 65-September 1, 2024

---

## Problem No 1:  
### Determine If a Number Is Even or Odd  
**Hint:** Check if the number is divisible by 2 without a remainder.  
**Formula:** If `num % 2 == 0`, the number is even; otherwise, it is odd.

```python
num = int(input("Enter num: "))
if num % 2 == 0:
    print(f"The number {num} is Even!")
else:
    print(f"The number {num} is Odd!")
```


## Problem No 2:  
### Determine If a Number Is Less Than, Greater Than, or Equal to Zero  
**Hint:** Compare the number with zero to determine its value.  
**Formula:** 
- If `num < 0`, the number is less than zero.
- If `num > 0`, the number is greater than zero.
- If `num == 0`, the number is zero.

```python
num = int(input("Enter num: "))
if num < 0:
    print("The number is less than zero!")
if num > 0:
    print("The number is greater than zero!")
if num == 0:
    print("The number is zero!")
```


## Problem No 3:  
### Check If a Number Is Divisible by 2 and 3  
**Hint:** Use modulo operations to check divisibility by 2 and 3.  
**Formula:** 
- If `num % 2 == 0` and `num % 3 == 0`, the number is divisible by both 2 and 3.
- If `num % 2 == 0`, the number is divisible by 2.
- If `num % 3 == 0`, the number is divisible by 3.

```python
num = int(input("Enter num: "))
if num % 2 == 0 and num % 3 == 0:
    if num % 2 == 0:
        print("The number is divisible by 2")
    elif num % 3 == 0:
        print("The number is divisible by 3")
else:
    print("The number is not divisible by 2 and 3")
```


## Problem No 4:  
### Determine Voter Eligibility Based on Age and Nationality  
**Hint:** Check if the person is 18 or older and has the specified nationality.  
**Formula:** 
- If `age >= 18` and `nationality == "pakistani"`, the person is eligible to vote.
- If the nationality is not "pakistani", the person needs a valid ID to vote.

```python
age = int(input("Enter the age: "))
nationality = (input("Enter your nationality: ")).lower()
if age >= 18:
    if nationality == "pakistani":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
```

---

## Problem No 5:  
### Categorize Age into Different Life Stages  
**Hint:** Use conditional statements to classify age into categories.  
**Formula:** 
- If `0 < age <= 12`, the person is a child.
- If `13 <= age <= 19`, the person is a teenager.
- If `20 <= age <= 59`, the person is an adult.
- If `60 <= age <= 98`, the person is a senior citizen.
- If `age < 0`, the age is invalid.
- If `age > 98`, the person is humorously considered "dead."

```python
age = int(input("Enter the age: "))
if 0 < age <= 12:
    print("You are a child")
elif 13 <= age <= 19:
    print("You are a teenager!")
elif 20 <= age <= 59:
    print("You are an adult!")
elif age >= 60:
    if age > 98:
        print("You are a dead man 😂!")
    else:
        print("You are a Senior citizen!")
elif age < 0:
    print("Invalid age")
else:
    print("Wrong age")
```

---

## Problem No 6:  
### Display the Name of the Month Based on the Month Number
## First way:
**Hint:** Use conditional statements to map the month number to the month name.  
**Formula:** 
- If `month_number` is between 1 and 12, print the corresponding month.
- If `month_number` is less than or equal to 0, print "Month number can't be negative!"
- If `month_number` is greater than 12, print "Only 12 months exist!"

```python
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
elif month_number <= 0:
    print("Month number can't be negative!")
else:
    print("Only 12 months exist!")
```
   
## Second Way:
 
**Hint:** Use the `match` statement to map the month number to the month name.  
**Formula:** 
- Use `case` to match the month number and print the corresponding month.
- Use `case _` to handle invalid month numbers.

```python
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
        print("Only 12 months exist!")
```

---

## Problem No 7:  
### Determine If a Year Is a Leap Year  
**Hint:** Use the leap year rules to determine if a year is a leap year.  
**Formula:** 
- A year is a leap year if it is divisible by 4 and (not divisible by 100 or divisible by 400).

```python
year = int(input("Enter the year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Yes, {year} is a leap year")
else:
    print(f"The {year} is not a leap year")
```

---
If need any help and wanna know more about me.
Lets connect.

<div style="text-align: center;">
    <a href="https://www.linkedin.com/in/your-profile" target="_blank" style="
        display: inline-block;
        padding: 8px 16px;
        color: #ffffff;
        background: linear-gradient(45deg, #ff4b5c, #6a1b9a);
        text-decoration: none;
        font-size: 14px;
        font-weight: bold;
        border-radius: 5px;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 5px;
        cursor: pointer;
    ">
        Visit My LinkedIn
        <span style="
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            animation: pulse 2s infinite;
        "></span>
    </a>
</div>

<style>
    @keyframes pulse {
        0% {
            transform: scale(0.9);
            opacity: 0.5;
        }
        50% {
            transform: scale(1.1);
            opacity: 0.3;
        }
        100% {
            transform: scale(0.9);
            opacity: 0.5;
        }
    }

    a:hover {
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.8); /* Stroke effect on hover */
        transform: scale(1.05); /* Slightly enlarge button on hover */
    }
</style>
---