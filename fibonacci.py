num1 = int(input("Enter your first number here: "))
num2 = int(input("Enter your second number here: "))
how_many_numbers = int(input("Enter how many numbers you want here: "))


def fibonacci(how_many_numbers, num1, num2):

    if how_many_numbers == 1:
        print(num1)
    else:
        print(num1)
        print(num2)

        for i in range(2, how_many_numbers):

            sequence = num1 + num2
            num1 = num2
            num2 = sequence

            print(sequence)


fibonacci(how_many_numbers, num1, num2)
