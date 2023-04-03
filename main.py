import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input("Enter a word : ").upper()
    try:
        result = [new_dic[x] for x in name]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
