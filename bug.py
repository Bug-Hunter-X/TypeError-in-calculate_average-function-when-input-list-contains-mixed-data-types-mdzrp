def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will output 0 which is correct

my_numbers = [10,20,30,40,50]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will output 30 which is correct

my_numbers = [10,20,30,40,50,'a']
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will throw an error