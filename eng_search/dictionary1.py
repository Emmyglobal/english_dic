# import anything necessary
import json
import tkinter as tk
from difflib import SequenceMatcher, get_close_matches

suggested_word = None

# Load the dictionary data
data = json.load(open("data.json"))

# Define the meaning check function
def check_meaning(word):

    global suggested_word

    close_words = get_close_matches(word, data.keys())[0]
    if word in data:
        return data[word]
    elif close_words and SequenceMatcher(None, word, close_words).ratio() >= 0.6:
        suggested_word = close_words
        return f"Did you mean '{suggested_word}'?  Click 'yes' or 'No'. "
    else:
        return "The word does not exist, please check again!"
def on_search():
    word = entry.get()
    if word.lower() in ['q', 'e']:
        root.quit()
    else:
        result = check_meaning(word.lower())
        if isinstance(result, list):
            result_text = "\n".join(result)
        else:
            result_text = result
        label_result.config(text=result_text)
def on_yes():
    if suggested_word:
        meanings = data.get(suggested_word, ["Nodefinition found."])
        result_text = "\n".join(meanings)
        label_result.config(text=result_text)
def on_no():
    label_result.config(text="The word does not exist, please check again!")
root = tk.Tk()
root.title("Simple Dictionary App")

# Create and place GUI elements
label_instruction = tk.Label(root, text="Enter a word to search:")
label_instruction.pack()

# Entry section
entry = tk.Entry(root)
entry.pack()

#create button
button_search = tk.Button(root, text="Search", command=on_search)
button_search.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_yes = tk.Button(frame_buttons, text="Yes", command=on_yes)
button_yes.grid(row=0, column=0, padx=5)

button_no = tk.Button(frame_buttons, text="No", command=on_no)
button_no.grid(row=0, column=1, padx=5)

# where the result will display
label_result = tk.Label(root, text="", wraplength=600, justify="left")
label_result.pack()

# Run the main event loop
root.mainloop()
