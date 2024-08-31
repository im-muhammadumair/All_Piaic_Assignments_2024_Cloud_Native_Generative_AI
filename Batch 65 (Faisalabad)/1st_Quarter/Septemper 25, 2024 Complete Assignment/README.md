

# PIAIC ASSIGNMENT-Batch 65-September 25, 2024

## Problem No 1:  
### Calculate Your Age Based on the Current Year and Your Birth Year
**Hint:** Calculate your age by subtracting your birth year from the current year.  
**Formula:** Age = Current Year - Birth Year

```python
def age_calculator(birth_year, current_year):
    print(f"Your age is {current_year-birth_year}")                            

print("Age calculator")
birth_year   = int(input("Enter your birth Year:   "))            
current_year = int(input("Enter your Current Year: "))
age_calculator(birth_year, current_year)
```


## Problem No 2:  
### Calculate the Area of a Circle Based on the Radius and Pi Value
**Hint:** The area of a circle is calculated by multiplying pi with the square of the radius.  
**Formula:** Area = π * (Radius²)

```python
def circle_area(radius, pie_value):
    print(pie_value * (radius**2))

radius = int(input("Enter the radius of the circle: "))
pie_value : float = 3.1416
circle_area(radius, pie_value)
```

## Problem No 3:  
### Calculate the Area of a Rectangle Based on Length and Width
**Hint:** The area of a rectangle is calculated by multiplying the length by the width.  
**Formula:** Area = Length * Width

```python
def rectangle_area(length, width):
    print(f"The area of rectangle is {length * width}")

length = int(input("Enter length: "))
width = int(input("Enter width:   "))
rectangle_area(length, width)
```

## Problem No 4:  
### Calculate the Volume of a Cube Based on Length, Width, and Height
**Hint:** The volume of a cube is calculated by multiplying the length, width, and height.  
**Formula:** Volume = Length * Width * Height

```python
def cube_area(length, width, height):
    print(f"The area of cube is {length * width * height}")

length = int(input("Enter length: "))
width = int(input("Enter width:   "))
height = int(input("Enter height: "))
cube_area(length, width, height)
```



## Problem No 5:  
### Convert Temperatures Between Celsius and Fahrenheit
**Hint:** Use the conversion formulas to convert temperatures between Celsius and Fahrenheit.  
**Formula:** Celsius = (Fahrenheit - 32) * 5/9  (-|-) Fahrenheit = (Celsius * 9/5) + 32

```PYTHON
def temp_fahrenheit(celsius):
    print(f"{celsius} celsius = {(celsius * 9/5) + 32} fahrenheit")

def temp_celsius(fahrenheit):
    print(f"{fahrenheit} fahrenheit = {(fahrenheit - 32) * 5/9} Celsius")

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = float(input("Enter temperature in fahrenheit: "))
temp_fahrenheit(celsius)
temp_celsius(fahrenheit)
```


## Problem No 6:  
### Convert Time from Minutes to Seconds
**Hint:** To convert minutes to seconds, multiply the time in minutes by 60.  
**Formula:** Seconds = Minutes × 60

```python
def second_minutes(time):
    print(f"{time} minutes = {(time * 60)} Seconds")

print("Time Calculator (Minutes -> Seconds)")
time = int(input("Enter your time in minutes: "))
second_minutes(time)
```

## Problem No 7:  
### Calculate Marks Based on Percentage and Total Marks
**Hint:** To calculate the marks based on the percentage, use the formula to find the proportion of the total marks.  
**Formula:** Marks = (Percentage / 100) × Total Marks

```python
def percentage_cal(percentage_value, total_marks):
    return (percentage_value / 100) * total_marks

print("Percentage Calculator")
percentage_value = int(input("Enter the percentage to calculate: "))
total_marks = int(input("Enter the total marks: "))
result = percentage_cal(percentage_value, total_marks)
print("The calculated marks are:", result)
```


## Problem No 8:  
### Calculate BMI (Body Mass Index) and Determine the Category
**Hint:** BMI is calculated using weight and height, and it helps determine the weight category.  
**Formula:** BMI = Weight / (Height²)

```python
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)  
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"
    
    print("Your BMI is:", bmi)
    print("Category:", category)

print("BMI Calculator")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_calculator(weight, height)
```

---

## Problem No 9:  
### Calculate the Volume of a Cylinder Based on Radius and Height
**Hint:** The volume of a cylinder is calculated using the formula that involves the radius and height.  
**Formula:** Volume = π * (Radius²) * Height

```python
def calculate_cylinder_volume(radius, height):
    pie_value = 3.1416
    volume = pie_value * (radius ** 2) * height
    print("Volume of Cylinder is:", volume)

print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))

calculate_cylinder_volume(radius, height)  
```

---