import json

data = json.load(open("data.json"))
# function retrieves words and definitions from json file
# input arg is a string (word) from user
# returns a string (definition)
def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    else: 
        return "Word does not exist in dictionary. Please double check it."    

word = input("Enter word: ")

print(define(word))