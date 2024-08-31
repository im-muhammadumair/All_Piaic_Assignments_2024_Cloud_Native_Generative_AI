def age_calculator(birth_year, current_year):
    print(f"Your age is {current_year-birth_year}")                            

print("Age calculator")
birth_year   = int(input("Enter your birth Year:   "))            # type: ignore
current_year = int(input("Enter your Current Year: "))
age_calculator( birth_year,current_year)


# # ---------------------------------------------------


def circle_area(radius, pie_value):
    print(pie_value*(radius**2))

radius = int(input("Enter the radius of circle: "))
pie_value : float = 3.1416
circle_area(radius, pie_value)


# # ---------------------------------------------------

def rectangle_area(length, width):
    print(f"The area of rectangle is {length*width}")

length = int(input("Enter length: "))
width = int(input("Enter width:   "))
rectangle_area(length,width)


# # ---------------------------------------------------

def cube_area(length, width, height):
    print(f"The area of cube is {length*width*height}")

length = int(input("Enter length: "))
width = int(input("Enter width:   "))
height = int(input("Enter height: "))
cube_area(length,width,height)


# # ---------------------------------------------------

def temp_fahrenheit(celsius):
    print(f"{celsius} celsius = {(celsius * 9/5) + 32} fahrenheit")

def temp_celsius(fahrenheit):
    print(f"{fahrenheit} fahrenheit = {(fahrenheit - 32) * 5/9} Celsius")

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = float(input("Enter temperature in fahrenheit: "))
temp_fahrenheit(celsius)
temp_celsius(fahrenheit)


# # ---------------------------------------------------

def second_minutes(time):
    print(f"{time} minutes = {(time*60)} Seconds")

print("Time Calculator (Minutes -> Seconds)")
time = int(input("Enter your time in minutes: "))
second_minutes(time)

# # ---------------------------------------------------
def percentage_cal(percentage_value, total_marks):
    return (percentage_value / 100) * total_marks

print("Percentage Calculator")
percentage_value = int(input("Enter the percentage to calculate: "))
total_marks = int(input("Enter the total marks: "))
result = percentage_cal(percentage_value, total_marks)
print("The calculated marks are:", result)

# # ---------------------------------------------------

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

# # ---------------------------------------------------

def calculate_cylinder_volume(radius, height):
    pie_value = 3.1416
    volume = pie_value * (radius ** 2) * height
    print("Volume of Cylinder is:", volume)

print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))

calculate_cylinder_volume(radius, height)  