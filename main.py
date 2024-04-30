"""
Multiplication Table
"""
# Provide your solution here


def print_multiplication_table(num1: int, num2: int):
    if num1 and num2 >= 1:
        for rows in (1, num2):
            result = num1 * rows
            print(f"{rows} * {num1} = {result}")
    else:
        print("Number and rows cannot be less than 1")




"""
Palindromes
"""


# Provide your solution here
def is_palindrome(text: str, palindrome: bool):
    if text[: len(text)] == [len(text), 0]:
        print("True")
    else:
        print("False")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
print_multiplication_table(-10,2)


