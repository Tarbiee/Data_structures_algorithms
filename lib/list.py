# pseudocode
# Create an empty list called no_duplicates to store unique elements.
# Iterate through each element in the input sequence.
# If the element is not already in the no_duplicates list, add it to the list.
# Return the list no_duplicates containing only unique elements.



def remove_duplicates(sequence):
    no_duplicates = []

    for number in sequence:
        if number not in no_duplicates:
             no_duplicates.append(number)

    return no_duplicates

print(remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5]))