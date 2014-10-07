#!/usr/bin/env python

from sys import argv
import random

def make_chunks(whole_text):
    """Takes a file, reads it and breaks it into pieces, passing each piece 
    into a dictionary, returns dictionary"""

    def make_chains(input_text):
        """Takes an input text as a string and updates a dictionary of
        markov chains."""

        chunk_text = input_text.split()

        for i in range(len(chunk_text)-2):
                
                key = (chunk_text[i], chunk_text[i+1])
                value = chunk_text[i+2]
                markov_chains.setdefault(key, []).append(value)
        #return markov_chains

    markov_chains = {}

    file_text = whole_text.read().split("\r\n")
    for chunk in file_text:
        make_chains(chunk)
    return markov_chains

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    lookup = random.choice(filter(lambda x: x[0][0].isupper(), chain_dict.keys()))
    sentence_list = [lookup[0], lookup[1]]
    while lookup in chain_dict:
        next_value = random.choice(chain_dict[lookup])
        sentence_list.append(next_value)
        lookup = (sentence_list[-2], sentence_list[-1])
    return " ".join(sentence_list)

def main(filename):
    chain_dict = make_chunks(open(filename))
    print make_text(chain_dict)

if __name__ == "__main__":
    script, filename = argv
    main(filename)
