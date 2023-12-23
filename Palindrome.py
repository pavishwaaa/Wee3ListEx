# Objective: Write a program to check
# if a list of characters forms a palindrome.

List1 = []

char = int(input("Enter number of element in list:"))

for i in range(0, char):
    element = input("Enter a single character as an elements:")
    List1.append(element)
print("Print original List: ", List1)

List2 = List1.copy()
List2.reverse()
print("Print reversed List: ", List2)

if List1 == List2:
    print("Palindrome")
else:
    print("Not palindrome")