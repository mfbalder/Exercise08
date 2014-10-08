#!/usr/bin/env python

from sys import argv
import random

def make_chunks(whole_text):
    """Takes a file, reads it and breaks it into pieces, passing each piece 
    into a dictionary, returns dictionary"""

    markov_chains = {}
    file_text = whole_text.read().split()

    stripped_text = []
    for i in range(len(file_text)):
        word = file_text[i].strip(',[]()"-_|')
        if word:
            stripped_text.append(word)

    for i in range(len(stripped_text)-2):
        key = (stripped_text[i], stripped_text[i+1])
        value = stripped_text[i+2]
        markov_chains.setdefault(key, []).append(value)

    return markov_chains

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    lookup = random.choice(filter(lambda x: x[0][0].isupper(), chain_dict.keys()))
    sentence_list = [lookup[0], lookup[1]]

    while lookup in chain_dict:
        next_value = random.choice(chain_dict[lookup])
        sentence_list.append(next_value)
        if next_value[-1] in ".?!":
            break
        lookup = (sentence_list[-2], sentence_list[-1])

    return " ".join(sentence_list)

def main(filename):
    chain_dict = make_chunks(open(filename))

    var1 = make_text(chain_dict)
    var2 = make_text(chain_dict)
    if len(var1 + var2) > 140:
        if len(var1) > 140:
            print make_text(chain_dict)
        print var1
        # print len(var1)
    else:
        print var1, var2
        # print len(var1 + var2)
    #print make_text(chain_dict), make_text(chain_dict)

if __name__ == "__main__":
    script, filename = argv
    main(filename)