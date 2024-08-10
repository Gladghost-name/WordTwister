from quick_anagram_solver import generate_anagrams
import streamlit as st

# 🚤
st.title("🌀 Word Twister")
st.write("🪢 Word Twister solves anagrams of any english word passed in,by generating anagrams of that word with varied lengths.The threshold parameter signifies the accuracy of words that are used as anagrams.I recommend that you use a threshold of .5 and above.")
col1, col2 = st.columns([.1, .2], gap="small")
# st.html("<a href='https://google.com'>Hello, World</a>")

temp_word = None

def fetch_anagrams():
    if word:
        anagrams = generate_anagrams(word, threshold)
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
    
exp = st.expander("Show/Hide Extra Options")
exp.text("👋 Extra Options Coming Soon")

if word and threshold:
    fetch_anagrams()

with col2:
    runbtn = st.button("GENERATE", type="primary", use_container_width=True)
    
