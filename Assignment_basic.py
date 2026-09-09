# Write a script that declares variables of each
#  type (int, float, str, bool), performs arithmetic
#  operations, and prints formatted output using f-strings.


age = 20                    # int
salary = 20000.50           # float
name = "John Doe"           # str
is_employed = True          # bool
tax = 0.15                    # float

# Arithhmatic Operations
new_salary = salary + 5000.25
tax_amount = new_salary * tax
net_salary = new_salary - tax_amount

# Formatted Output
print(f"Employee Name: {name}")
print(f"Employee Age: {age}")
print(f"Employee Salary: £{salary:.2f}")
print(f"Employee Is Employed: {is_employed}")
print(f"New Salary: £{new_salary:.2f}")
print(f"Tax Amount: £{tax_amount:.2f}")
print(f"Net Salary: £{net_salary:.2f}")


#Implement a function that accepts two numbers and 
# returns their sum, difference, product, and 
# quotient as a tuple — call it with at least 
# three different input pairs.

def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None
    return (sum_result, difference_result, product_result, quotient_result) 

# Call the function with different input pairs
result1 = calculate_operations(10, 5)
result2 = calculate_operations(20, 4)
result3 = calculate_operations(15, 3)

print("Results for (10, 5):", result1)
print("Results for (20, 4):", result2)
print("Results for (15, 3):", result3)

#  Use a for loop with range() to generate
#  a multiplication table (1–10) and print
#  it in a formatted grid.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")
    print()  # New line after each row


#Write a temperature converter that reads
#  a value and unit (C/F) and uses
#  if/elif/else to convert and display the result.

temperature = float(input("Enter temperature: "))
unit = input("Is this C or F:")

if unit == "C":
    answer = (temperature * 9/5) + 32
    print(f"{temperature} C is {answer:.2f} F")
elif unit == "F":
    answer = (temperature - 32) * 5/9
    print(f"{temperature} F is {answer:.2f} C")
else:
    print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")