# Markov Chaining algorithm

import random

def markov_chain():
    # handle filepaths
    file_paths = "/Users/deloschang/Documents/self_projects/standalone_markov/corpus.txt" # Bob Dylan songs file input
    file = open(file_paths)

    # initialize markov dictionary
    markov_chain = {}

    # 
    first_word = "\n"

    print "Start reading the lines..."

    for eachline in file:
        # split by space
        for current_word in eachline.split():

            # as long as word not empty
            if current_word != "":
                markov_chain.setdefault((first_word), []).append(current_word)

                first_word = current_word

    return markov_chain
 

def construct_markov(markov_chain, word_count):
    print "Constructing..."

    generate = ""

    choices = random.choice( markov_chain.keys() )
    first_word = choices
    
    for i in xrange(word_count):
        try:
            new_word = random.choice(markov_chain[(first_word)])
        except KeyError: 
            # reached the end! 
            break

        generate = generate + " " + new_word
        first_word = new_word
        
    return generate

markov_output = markov_chain()

# default word count to 50 
print "---Output----"
print construct_markov(markov_output, 50)

