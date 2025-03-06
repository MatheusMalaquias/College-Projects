#I added a delay to appear the results
import random
import time
 
def get_determiner(word):
    if word == 1:
        word = ["a", "one", "the"]
    else:
        word = ["some", "many", "the"]
    words = random.choice(word)
    return words

def get_determiner_2(word):
    if word == 1:
        word = ["a", "one", "the"]
    else:
        word = ["some", "many", "the"]
    words = random.choice(word)
    return words

def get_determiner_3(word):
    if word == 1:
        word = ["a", "one", "the"]
    else:
        word = ["some", "many", "the"]
    words = random.choice(word)
    return words
           
def get_noun(noun):
    if noun == 1:
        noun = ['bird', 'boy', 'car','cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        noun = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']
    nouns = random.choice(noun)
    return nouns

def get_noun_2(noun):
    if noun == 1:
        noun = ['bird', 'boy', 'car','cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        noun = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']
    nouns = random.choice(noun)
    return nouns

def get_noun_3(noun):
    if noun == 1:
        noun = ['bird', 'boy', 'car','cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        noun = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']
    nouns = random.choice(noun)
    return nouns
 
def get_verb(word, verb):
    if verb == 'past':
        verb = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']   
    elif verb == 'present' and word == 1:
        verb = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']             
    elif verb == 'present' and word != 1:
        verb = ['drin', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']        
    elif verb == 'future':
        verb = ['will drink', 'will eat', 'will grow','will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']
    verbs = random.choice(verb)
    return verbs

def get_preposition():
    preposition = ['about', 'above', 'across', 'after', 'along', 'around', 'at', 'before', 'behind', 'below', 'beyond', 'by', 'despite', 'except', 'for', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'onto', 'out', 'over', 'past', 'to', 'under', 'with', 'without']
    prepositions = random.choice(preposition)
    return prepositions

def get_preposition_2():
    preposition = ['about', 'above', 'across', 'after', 'along', 'around', 'at', 'before', 'behind', 'below', 'beyond', 'by', 'despite', 'except', 'for', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'onto', 'out', 'over', 'past', 'to', 'under', 'with', 'without']
    prepositions = random.choice(preposition)
    return prepositions
    
def make_sentence(word, verb):
    determiner = get_determiner(word)
    noun = get_noun(word)
    prepositions = get_preposition()
    determiner_2 = get_determiner(word)
    noun_2 = get_noun(word)
    verbs = get_verb(word, verb)
    prepositions_2 = get_preposition_2()
    determiner_3 = get_determiner(word)
    noun_3 = get_noun(word)
    return determiner.capitalize(), noun,prepositions, determiner_2, noun_2, verbs, prepositions_2, determiner_3, noun_3

def main():
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
    time.sleep(2)
    a, b, c, d, e, f, g, h, i= make_sentence(1, 'past')
    print(a, b, c, d, e, f, g, h, i)
main()