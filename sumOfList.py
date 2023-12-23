# Objective: Create a program that
# calculates the sum of all elements in a list.

numList = []

num = int(input("Enter number of element in list:"))

for i in range(0, num):
    element = int(input("Enter elements:"))
    numList.append(element)

print("Largest element in the list: ", sum(numList))

