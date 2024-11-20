#Write a Python program to find the first non-repeating elements in a given list of integers
A = [10,20,20,30,40,40,10,50]
nonrepeated_element = set()
repeated_element = set()

for i in A:
    #If i is already in repeated_element , skip to the next iteration.
    # This ensures we don't process duplicates multiple times
    if i in repeated_element:
        continue
        # Check if i is already in nonrepeated_element .
    if i in nonrepeated_element:
        nonrepeated_element.remove(i)
        repeated_element.add(i)
    else:
        nonrepeated_element.add(i)

print(list(nonrepeated_element))