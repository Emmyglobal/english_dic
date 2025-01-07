import json
import tkinter as tk
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
while(True):
    def check_meaning(word):
        close_word = get_close_matches(word, data.keys())
        if word in data:
            return (data[word])
        elif word.capitalize() in data:
            return (data[word.capitalize()])
        elif word.upper() in data:
            return (data[word.upper()])
        elif len(close_word) > 0:
            print("Did you mean {}?".format(close_word[0]))
            options = input("Type Y if Yes or N if No: ")
            if options.upper() == "Y":
                return (data[close_word[0]])
            elif options.upper() == "N":
                return ("The word does not not exist, please check again!")
            else:
                return ("Your input is beyond our understanding, Please try again.")
        else:
            return ("The word does not not exist, please check again!")
    user_word = input("Search a word: ")
    if user_word.lower() == 'q' or user_word.lower() == 'e':
        break
    result = check_meaning(user_word.lower())
    if type(result) == list:
        for values in result:
            print(values)
    else:
        print(result)
