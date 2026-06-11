# Python Basics: Syntax, Variables, and Input/Output

print("===================================")
print("   WELCOME TO PYTHON PROGRAMMING   ")
print("===================================\n")

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
cgpa = float(input("Enter your CGPA: "))

# Variables and Data Types
is_student = True

# Output user details
print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Age:", age)
print("College:", college)
print("CGPA:", cgpa)
print("Student Status:", is_student)

# Arithmetic Operations
next_year_age = age + 1
birth_year = 2026 - age

print("\n----- CALCULATIONS -----")
print("Your age next year will be:", next_year_age)
print("Approximate birth year:", birth_year)

# String Operations
print("\n----- STRING OPERATIONS -----")
print("Name in Uppercase:", name.upper())
print("Name in Lowercase:", name.lower())
print("Length of Name:", len(name))

# Conditional Statements
print("\n----- PERFORMANCE ANALYSIS -----")

if cgpa >= 9.0:
    print("Excellent Performance!")
elif cgpa >= 8.0:
    print("Very Good Performance!")
elif cgpa >= 7.0:
    print("Good Performance!")
else:
    print("Keep Improving!")

# Final Message
print("\nThank you for learning Python!")
print("Have a great day,", name + "!")
