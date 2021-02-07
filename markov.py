"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)  
    text = file.read()
    file.close()
    # print(text)
    return text
   



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    words = text_string.split()

    # To set a stop point, append None to the end of our word list.

    words.append(None)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    print(chains)
    return chains
    

   



def make_text(chains):
    """Return text from chains."""
    words = []
#{('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
    for key in chains:
        #print(key, chains[key])
        
        random_word = choice(chains[key])
        new_key = (key[1], random_word)
        print (new_key)

        if new_key in chains:

            new_random_word = choice(chains[new_key])
            if new_random_word is None:
                break
            else:

                words.append(new_random_word)

        else:
            break

    print (words)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

