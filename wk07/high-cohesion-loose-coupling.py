def get_num(question):
    num = int(input(question))
    return num


def add(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

count = get_num("How many values would you like to add? ")
numbers = []
for i in range(0, count):
    numbers.append(get_num("Enter a number: "))
answer = add(numbers)
print("The sum of the numbers is: %d" % (answer))
