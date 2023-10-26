numbers = input("Введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]
with open('numbers.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + ' ')
with open('numbers.txt', 'r') as file:
    numbers_str = file.read().split()
    numbers = [int(num) for num in numbers_str]
sum_of_numbers = sum(numbers)
print(f"Сумма чисел: {sum_of_numbers}")
