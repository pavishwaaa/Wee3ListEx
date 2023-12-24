
# Objective: Create a program that finds
# common elements in two lists.

def common_element(a, b):
    com = []
    for ele in a:
        if ele in b and ele not in com:
            com.append(ele)
    return com


a = [1, 2, 3, 4]
b = [2, 4, 1, 7, 8]

com = common_element(a, b)
print("Common elements: ", com)

