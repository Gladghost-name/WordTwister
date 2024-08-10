import math
import numpy
import string

alphabets = string.ascii_lowercase

# loading all the words as text from the dictionary (A less optimized method)
f = open("WordTwister/updated_words.txt", "r+")
content = f.read().splitlines() # splitting into individual words.

def generate_coefficent(target_word, word):
    target_mapping = 0
    mapping = 0

    for letter in target_word:
        mapping += (target_word.count(letter.lower())/len(target_word)) * (alphabets.index(letter.lower())+1)
    
    mapping_sum = mapping/(1/len(target_word))
    for letter in word:
        target_mapping += (target_word.count(letter.lower())/len(target_word)) * (alphabets.index(letter.lower())+1)
    return (target_mapping/(1/len(target_word))/mapping_sum)/(len(word)/len(target_word))

def generate_word_mapping(word):
    map = {}
    for letter in word:
        if letter not in map.keys():
            map[letter] = word.count(letter)
    return map

def compare_mapping(tw, w, m1, m2):
    temp_m = []
    for v in m2:
        if v in m1.keys():
            temp_m.append(m2[v] - m1[v])
        else:
            temp_m.append(999)
    temp_m = numpy.array(temp_m)
    return math.exp(-numpy.linalg.norm(temp_m*(len(w)/len(tw))))

def generate_anagrams(target_word, threshold):
    corpus = content
    grouped_anagrams = {}
    mapping = generate_word_mapping(target_word.lower())
    for word in corpus:
        if len(target_word) >= len(word) >= 2 and word[0].lower() in target_word.lower():
            coefficent = compare_mapping(target_word, word, mapping, generate_word_mapping(word.lower()))
            if coefficent >= threshold:
                if len(word) not in grouped_anagrams.keys():
                    grouped_anagrams[len(word)] = []
                if word not in grouped_anagrams[len(word)]:
                    grouped_anagrams[len(word)].append(word)
    return grouped_anagrams


# For testing sake!!
# anagrams = generate_anagrams("computer", .7)
# sorted_dict = sorted(anagrams)[::-1]
# for k in sorted_dict:
#     print(f"{k} Letter Words\n\n{' '.join(anagrams[k])}\n")