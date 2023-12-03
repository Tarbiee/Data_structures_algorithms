# pseudocode
# Split the input sentence into a list of words using a space as a delimiter.
# Create an empty dictionary called dict to store word frequencies.
# Iterate through each word in the list.
# If the word is not a key in the dictionary, add it with an initial value of 0.
# Increment the value associated with the current word in the dictionary by 1.
# Return the populated dictionary.


def word_frequency(sentence):
    words = sentence.split()# splits the sentence into a list of words
    dict = {}

    for word in words:
        if word not in dict.keys():
            dict[word] = 0

        dict[word] = dict[word]+ 1

    return dict

print(word_frequency("This is a test sentence. This sentence is a test."))
