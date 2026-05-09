# Get first number from user
#Get operator from user (+, -, *, /, etc.)
#Get second number from user
#
#Perform the arithmetic operation based on the given operator
#Return the computed result
#
#Call the function
#Print the final result
#

first_number = int(input("Enter first number: "))
operator = input("Enter operator: ")
second_number = int(input("Enter second number: "))


def calculate(first_number, operator, second_number):
    match operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            result = first_number / second_number

    return result
    
result =  calculate(first_number, operator, second_number)
 
print(result)
