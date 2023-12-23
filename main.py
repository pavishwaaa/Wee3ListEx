# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Write a program to find the largest number in a list provided by the user.

numList = []

num = int(input("Enter number of element in list:"))

for i in range(0, num):
    element = int(input("Enter elements:"))
    numList.append(element)

print("Largest element in the list: ", max(numList))


