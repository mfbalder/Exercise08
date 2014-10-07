#!/usr/bin/env python

from sys import argv
import random

def make_chains(input_text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chains = {}
    file_text = input_text.read().replace("\n", " ").split()
    #print file_text
    for i in range(len(file_text)-2):
            
            key = (file_text[i], file_text[i+1])
            value = file_text[i+2]
            # if key not in markov_chains:
            #     markov_chains[key] = [value]
            # else:
            #     markov_chains[key].append(value)
            markov_chains.setdefault(key, []).append(value)
    return markov_chains

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    start = random.choice(chain_dict.keys())

    return "Here's some random text."

def main():
    # args = sys.argv
    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename)

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
