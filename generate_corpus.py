import string

punctuations = string.ascii_lowercase

f = open("Vocabularies/fra_100k-words.txt", "rb+")
sections = f.read().splitlines()

words = []


for section in sections:
    try:
        section = section.decode()
        word = section.split()[1].lower()
        joined_word = []
        for char in str(word):
            if str(char.lower()) not in punctuations:
                break
            joined_word.append(char)
        if len(joined_word) == len(word) and len(word) >= 2 and word not in words:
            words.append(word)
    except:
        pass

f = open("Vocabularies/fra_100k-words.txt", "w+")
f.write("\n".join(sorted(words)))
    
