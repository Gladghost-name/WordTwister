f = open("Vocabularies/fra_100k-words.txt", "r+")
words = f.read().splitlines()

wds = []
for idx, word in enumerate(words):
    print(idx+1, "/", len(words))
    if word not in wds:
        wds.append(word)
        
f.close()

f = open("Vocabularies/fra_100k-words.txt", "w+")
f.write("\n".join(wds))

