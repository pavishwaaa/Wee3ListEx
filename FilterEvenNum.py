# Objective: Develop a program that filters out
# odd numbers
# from a list and prints the remaining even numbers.

numList = []

num = int(input("Enter number of element in list:"))

for i in range(0, num):
    element = int(input("Enter elements:"))
    numList.append(element)


def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0


oddNum = list(filter(is_odd, numList))
evenNum = list(filter(is_even, numList))

print("Odd numbers:", oddNum)
print("Even numbers:", evenNum)
