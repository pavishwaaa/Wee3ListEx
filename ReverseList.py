# Objective: Develop a program that reverses a list
# without using the built-in reverse function.

List1 = [1,2,3,4,5]
listLen = len(List1)
List2 = []

for i in List1:
    List2.insert(0,i)  # keep inserting Original list elements to index 0. Which will reverse list eventually.

print("Reversed list is: ", List2)
