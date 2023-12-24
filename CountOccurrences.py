# Objective: Write a program that counts how
# many times an element occurs in a list.

def countOccurrences(input_list):
    elements_count = {}

    for element in input_list:
        if element not  in elements_count:
            elements_count[element] = 1
        else:
            elements_count[element] += 1

    return elements_count


user_input = input("Enter elements separated by spaces: ")
user_list = user_input.split()

occurrences = countOccurrences(user_list)

for element, count in occurrences.items():
    print(f"{element}: {count} times")

