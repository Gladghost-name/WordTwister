from quick_anagram_solver import generate_anagrams
import streamlit as st

# 🚤
st.title("🌀 Word Twister")
st.write("🪢 Word Twister solves anagrams of any word passed in,by generating anagrams of that word with varied lengths.The threshold parameter signifies the accuracy of words that are used as anagrams.I recommend that you use a threshold of .5 and above.")
col1, col2 = st.columns([.1, .2], gap="small")

temp_word = None

def filtered(word):
    truth_map = []
    if language == "French ⚠️ Coming Soon!":
        return False
    if ex_word:
        if ex_options == "As Suffix":
            if ex_word in word[:len(ex_word)]:
                if len(word) == int(fixed_word_length) and use_word_length == True:
                    return True
                elif use_word_length == True and len(word) != int(fixed_word_length):
                    return False
                else:
                    return True
        elif ex_options == "As Prefix":
            if ex_word in word[len(word) - len(ex_word):]:
                if len(word) == int(fixed_word_length) and use_word_length == True:
                    return True
                elif use_word_length == True and len(word) != int(fixed_word_length):
                    return False
                else:
                    return True
        elif ex_options == "AnyWhere":
            if ex_word in word:
                if len(word) == int(fixed_word_length) and use_word_length == True:
                    return True
                elif use_word_length == True and len(word) != int(fixed_word_length):
                    return False
                else:
                    return True
        return False
    
    if len(word) == int(fixed_word_length) and use_word_length == True:
                    return True
    elif use_word_length == True and len(word) != int(fixed_word_length):
        return False
    return True

def fetch_anagrams():
    if word:
        anagrams = generate_anagrams(word, threshold, filtered)
        sorted_dict = sorted(anagrams)[::-1]
        results_found = sum([len(anagrams[result]) for result in sorted_dict])
        if results_found > 0:
            st.write(f"{results_found} results found.")
        else:
            st.write("No result Found!")
        for k in sorted_dict:
            expander = st.expander(f"{k} Letter Words", icon="⚡", expanded=True)
            formatted_string = ""
            for value in anagrams[k]:
                formatted_string += f"<a href='https://en.wikipedia.org/wiki/{value}' target='_blank'>{value}</a>\t"
            expander.html(formatted_string)

with col1:
    word = st.text_input("Enter a Word", placeholder="Enter Word", label_visibility="collapsed")
    threshold = st.number_input("Enter a Threshold", 0.0, 1.0, .7, placeholder="Enter Threshold")
    
with st.expander("Show/Hide Extra Options"):
    excol1, excol2 = st.columns(2)

    with excol1:
        ex_word = st.text_input("Specify the word to be visible in the anagram generated.", placeholder="Extra Word")


    with excol2:
        ex_options = st.selectbox("Specify position of word in generated anagram.", ["As Suffix", "As Prefix", "AnyWhere"])

    language = st.selectbox("Select Language", options=["English", "French ⚠️ Coming Soon!"])
    
    use_word_length = st.checkbox("Set Fixed Word Length")
    fixed_word_length = st.number_input("Enter a fixed word length", disabled=not use_word_length, placeholder="Input Word Length")
if word and threshold:
    fetch_anagrams()

with col2:
    runbtn = st.button("GENERATE", type="primary", use_container_width=True)
    
