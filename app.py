import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# function retrieves words and definitions from json file
# input arg is a string (word) from user
# returns a string (definition)
def define(word):
    word = word.lower()
    if word in data:
        return '\n'.join(data[word])
    elif word.title() in data:
        return '\n'.join(data[word.title()])
    elif word.upper() in data:
        return '\n'.join(data[word.upper()])    
    elif  get_close_matches(word, data.keys()):
        match = get_close_matches(word, data.keys())[0]
        reply = input("Did you mean %s? Enter Y if yes, or N if no" %match)
        if reply == "Y":
            return '\n'.join(data[match])
        else:
            return "Word does not exist in dictionary. Please double check it."  
    else: 
        return "Word does not exist in dictionary. Please double check it."    

word = input("Enter word: ")

print(define(word))