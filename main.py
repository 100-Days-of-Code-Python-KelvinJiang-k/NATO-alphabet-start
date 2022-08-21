student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

{"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_name = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# nato_name = {letter: nato_alphabet[nato_alphabet["letter"] == letter].code for letter in name}

name = input("What is your name?  ").upper()
print(name)

nato_wordlist = [nato_name[letter] for letter in name]
print(nato_wordlist)
