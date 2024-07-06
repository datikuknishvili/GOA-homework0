numbers = [6,10,14,23,35,47]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)

numbers.pop(5)
print(numbers)





numbers = [6,10,14,23,35,47]

min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(min_number)

numbers.pop(0)
print(numbers)
