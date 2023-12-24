
# Objective: Write a program that removes
# duplicates from a list.

def Remove(List1):
    final_list = []
    for num in List1:
        if num not in final_list:
            final_list.append(num)
    return final_list


List1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
print(Remove(List1))


