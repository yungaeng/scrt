def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]

squares = map(square, numbers)
squares_list = list(squares)
print(squares_list)

squares = map(lambda n: n ** 2, numbers)
print(list(squares))

print(max(numbers), min(numbers))

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
heights = [180.5, 172.1, 185.3]

zipped = zip(names, ages, heights)
print(list(zipped))
print(list(zipped))
