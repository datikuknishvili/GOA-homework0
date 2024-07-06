numbers = [2,4,6,8,13,45,87,56,]

min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(min_number)

numbers = [2,4,6,8,13,45,87,56,]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)

numbers = [2,4,6,8,13,45,87,56,]

sum_numbers = 0

for number in numbers:
    sum_numbers = sum_numbers + number

print(sum_numbers)
