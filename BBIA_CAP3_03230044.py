# https://github.com/decwangg/03230044_BIA101_CAP3
# Dechen Wangmo
# BBI 'A'
# 03230044
# References
# https://youtu.be/qjrRf_pXWFQ?si=B4Xbm6Kk3FnHCF5q
# https://youtube.com/playlist?list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd&si=IaAtCAKC8Io3RqgB
# https://youtu.be/4NvLznuITH0?si=nf_R9cvzkRvMHWBs
# Solution
# Solution Score : 492603


# Read the input.txt file
def read_input(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []

# Function to extract the required two-digit number from each line
def extract_number(line):
    # Manually find all digits in the line
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    if len(digits) >= 2:
        # Take the first and last digit and form the two-digit number
        number = int(digits[0] + digits[-1])
    elif len(digits) == 1:
        # If there is only one digit, form a two-digit number by doubling it
        number = int(digits[0] * 2)
    else:
        number = 0
    return number

# Solution to calculate the total sum and keep track of each line's number
def calculate_sum(file_name):
    lines = read_input(file_name)
    total_sum = 0
    line_details = []
    for line in lines:
        number = extract_number(line)
        total_sum += number
        line_details.append((line.strip(), number))
    return total_sum, line_details

# Print the solution
def print_solution(file_name):
    total_sum, line_details = calculate_sum(file_name)
    for i, (line, number) in enumerate(line_details):
        print(f"Line {i + 1}: '{line}' -> {number}")
    print(f"The total sum from the given input file {file_name} is {total_sum}")


file_name = '044.txt'  

# Execute the function to display the outcome
print_solution(file_name)


