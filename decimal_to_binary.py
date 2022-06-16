def decimalToBinary(number):
    binary_number =[]
    while number != 0:
        binary_number.append(number % 2)
        number = number // 2
    return binary_number[::-1]

print(decimalToBinary(42))


