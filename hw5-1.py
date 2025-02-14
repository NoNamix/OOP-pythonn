import random


class Encryptor:
    def __init__(self, *numbers):
        self.__numbers = numbers
        self.__result = self.__encrypt()

    def __encrypt(self):
        operation = random.choice(["+", "-", "*", "/"])
        result = self.__numbers[0]
        for num in self.__numbers[1:]:
            if operation == "+":
                result += num
            elif operation == "-":
                result -= num
            elif operation == "*":
                result *= num
            elif operation == "/" and num != 0:
                result /= num
        return result

    def __str__(self):
        return f"Encrypted result: {self.__result}"


encrypted = Encryptor(10, 5, 2)
print(encrypted)