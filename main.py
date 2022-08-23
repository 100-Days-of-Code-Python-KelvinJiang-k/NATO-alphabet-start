import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_name = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

name = input("What is your name?  ").upper()


def generate_phonetic():
    try:
        nato_wordlist = [nato_name[letter] for letter in name]
    except KeyError:
        print("Invalid name input; only letters are allowed.")
        generate_phonetic()
    else:
        print(nato_wordlist)

generate_phonetic()
