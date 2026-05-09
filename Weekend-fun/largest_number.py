first_number = int(input("Enter number_one: "))
second_number = int(input("Enter number_two: "))
third_number= int(input("Enter number_three: "))

largest = first_number

if second_number > first_number:
    largest = second_number
elif third_number > second_number:
    largest = third_number
    
print(largest)

