# PIAIC ASSIGNMENT-September 18, 2024

## Problem No 1:  
### Calculate Your Age Based on the Current Year and Your Birth Year
**Hint:** Calculate your age by subtracting your birth year from the current year.  
**Formula:** Age = Current Year - Birth Year

```python
print("Age Calculator")
birth_year = int(input("Enter your Birth-Year: "))
current_year = int(input("Enter your Current-Year: "))
print("Your age is ", (current_year - birth_year))
```


## Problem No 2: Calculate the Area of a Rectangle Using Length and Width Variables
**Hint:** Calculate the area of a rectangle using its length and width.  
**Formula:** Area = Length * Width

```python
print("Rectangle Area Calculator")
rectangle_length = int(input("Enter your Rectangle-length: "))
rectangle_width = int(input("Enter your Rectangle-Width: "))
print("The area of your rectangle is ", (rectangle_length * rectangle_width))
```


## Problem No 3: Calculate the Area of a Circle
**Hint:** Calculate the area of a circle using its radius.  
**Formula:** Area = π * radius²

```python
print("Circle Area Calculator")
circle_radius = int(input("Enter your circle-radius: "))
pie_value = 3.1416
print("The area of the circle is: ", (pie_value * (circle_radius ** 2)))
```


## Problem No 4: Calculate the Volume of a Cube
**Hint:** Calculate the volume of a cube using its side length.  
**Formula:** Volume = side³

```python
print("Cube Volume Calculator")
cube_length = int(input("Enter your Cube-Length: "))
cube_width  = int(input("Enter your Cube-Width: "))
cube_height = int(input("Enter your Cube-Height: "))
print("The volume of the Cube is: ", (cube_length * cube_width * cube_height))
```


## Problem No 5: Convert a Temperature from Fahrenheit to Celsius and Vice Versa
**Hint:** Took userinput of temperature from user as Fahrenheit to Celsius and vice versa  
**Formula:** Celsius = (Fahrenheit - 32) * 5/9  -|-  Fahrenheit = (Celsius * 9/5) + 32

```python
Print("\t Temperature Calculator")

print("Temperature Convertor (Celsius -> Fahrenheit)")
temperature = int(input("Enter your temperature in Celsius: "))
print("Temperature in Fahrenheit is: ", ((temperature * 9 / 5) + 32))

print("Temperature Convertor (Fahrenheit -> Celsius)")
temperature = int(input("Enter your temperature in Fahrenheit: "))
print("Temperature in Celsius is: ", ((temperature - 32) * 5 / 9))
```


## Problem No 6: Convert a Given Number of Seconds into Minutes and Seconds
**Hint:** Take input from the user in seconds, convert it into minutes, and vice versa.  
**Formula:** Minutes = Seconds // 60

```python
print("Time Calculator (Minutes -> Seconds)")
time_minutes = int(input("Enter your time in minutes: "))
print("Time in seconds is: ", (time_minutes * 60))
```


## Problem No 7: Calculate the Percentage
**Hint:** Take input for the total value and the part of it, multiply it and then divide by 100.
**Formula:** Percentage = (Part / Total) * 100

```python
print("Percentage Calculator")
percentage = int(input("Enter your percentage: "))
marks = int(input("Enter your marks: "))
print("Percentage is: ", ((percentage / 100) * marks))
```


## Problem No 8: Calculate the BMI Using Height and Weight
**Hint:** Calculate the Body Mass Index (BMI) using height and weight.  
**Formula:** Weight / (Height)²

```python
print("BMI Calculator")
weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print('Overweight')
else:
    print('Obesity')
```


## Problem No 9: Calculate the Volume of a Cylinder
**Hint:** Calculate the volume of a cylinder using its radius and height.  
**Formula:** Volume = π * (radius)² * height

```python
print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
pie_value = 3.1416
print("Volume of Cylinder is: ", pie_value * (radius ** 2) * height)
```