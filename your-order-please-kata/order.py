#!/usr/bin/env python3
import re
"""Takes a string as input and sorts it according to
the number that each word contains """
def order_sentence(sentence):
    # Return an empty string in case
    # the input sentence is empty
    if sentence == '':
        return ''
    # Turn input string into a list
    word_list = sentence.split()
    # Size of the list stored in a variable plus 1
    words_number = len(word_list) + 1
    # Initializing an empty list to return
    ans = []
    # Loop from 1 to words_number
    for number in range(1,words_number):
        # Pattern to locate word with current number
        pattern = r" *(([a-zA-Z]*)*"+str(number)+r"[a-zA-Z]*) *"
        # Obtain word that matches current number
        word = re.search(pattern,sentence).group(1).strip()
        # Append new word to the final answer
        ans.append(word)
    # Turn ans into a string
    return ' '.join(ans)

        

