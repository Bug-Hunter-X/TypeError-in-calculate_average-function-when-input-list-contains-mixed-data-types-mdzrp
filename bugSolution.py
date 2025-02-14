def calculate_average(numbers):
    try:
        if not numbers:
            return 0
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: The input list contains mixed data types. Please provide a list of numbers only.")
        return None

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10,20,30,40,50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10,20,30,40,50,'a']
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will not throw an error