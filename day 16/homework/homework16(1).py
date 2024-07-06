numbers = [5, 3, 8, 2, 9, 1]

smallest = numbers[0]  # assume the first number is the smallest

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

