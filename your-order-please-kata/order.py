#!/usr/bin/env python3
"""Takes a string as input and sorts it according to
the number that each word contains """
def order_sentence(sentence):
    # Return an empty string in case
    # the input sentence is empty
    if sentence == '':
        return ''
    # Turn input string into list
    word_list = sentence.split()
    
