#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import streamlit as st
import unicodedata

def gnome_style(word, add_g_prefix=False):
    vmap = {
        'a': ['â', 'à', 'ä', 'á', 'a'],
        'e': ['ê', 'è', 'ë', 'é', 'e'],
        'i': ['ï', 'î', 'ì', 'í', 'i'],
        'o': ['ô', 'ö', 'ò', 'ó', 'o'],
        'u': ['û', 'ü', 'ù', 'ú', 'u'],
        'y': ['ÿ', 'y'],
        't': ['†', 't']
    }
    lw = word.lower().strip(",.!?")
    if lw.startswith("n") and random.random() < 0.8:
        word = "gn" + word
    elif lw[0] in "aeiou" and random.random() < 0.15:
        word = "g" + word
    elif add_g_prefix and word and word[0].lower() not in "g'":
        word = "g'" + word
    new_word = ""
    for c in word:
        if c in vmap and random.random() < 0.8:
            new_word += random.choice(vmap[c])
        elif c.lower() == "n" and random.random() < 0.2:
            new_word += "ñ"
        elif c == "'":
            new_word += random.choice(["'", "’"])
        else:
            new_word += c
    return new_word

def gnome_stylize_sentence(sentence):
    words = sentence.split()
    out = []
    for idx, w in enumerate(words):
        add_g = random.random() < 0.33
        if w.lower() == "i":
            out.append("Ï")
        else:
            out.append(gnome_style(w, add_g))
    return " ".join(out)

def de_gnomeify_word(word):
    orig = word
    for prefix in ["g'", "gn", "g"]:
        if word.startswith(prefix):
            word = word[len(prefix):]
            break
    word = word.replace('â','a').replace('à','a').replace('ä','a').replace('á','a')
    word = word.replace('ê','e').replace('è','e').replace('ë','e').replace('é','e')
    word = word.replace('ï','i').replace('î','i').replace('ì','i').replace('í','i')
    word = word.replace('ô','o').replace('ö','o').replace('ò','o').replace('ó','o')
    word = word.replace('û','u').replace('ü','u').replace('ù','u').replace('ú','u')
    word = word.replace('ÿ','y')
    word = word.replace('†','t')
    word = word.replace('ñ','n')
    word = ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )
    word = word.replace("’", "'")
    if orig == "Ï":
        word = "I"
    return word

def de_gnomeify_sentence(sentence):
    return " ".join(de_gnomeify_word(w) for w in sentence.split())

def to_fraktur(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    fraktur = [
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
    ]
    mapping = {c: f for c, f in zip(normal, fraktur[0] + fraktur[1])}
    return ''.join(mapping.get(ch, ch) for ch in text)

# ---- Streamlit UI ----
st.set_page_config(page_title="Gnome Translator", page_icon="🧙‍♂️")

st.markdown(
    "<h1 style='font-size:2.7em; font-family:serif;'>🧙‍♂️ Gnome Translator</h1>",
    unsafe_allow_html=True
)
headline = "What’s the Garden G’nossip?"
st.markdown(
    f"<div style='font-size:2em; color:#264813; margin-bottom:16px'>{to_fraktur(headline)}</div>",
    unsafe_allow_html=True
)

st.write("Type English below to see Gnome fantasy text and the reverse translation:")

# --- Box 1: English to Gnome ---
text = st.text_area("Enter English text:", "")

if text:
    gnomified = gnome_stylize_sentence(text)
    st.markdown("**Gnome-ified:**")
    st.markdown(f"<div style='font-size:1.4em'>{gnomified}</div>", unsafe_allow_html=True)
    st.markdown("**Gnome-ified (Fraktur):**")
    st.markdown(f"<div style='font-size:1.1em'>{to_fraktur(gnomified)}</div>", unsafe_allow_html=True)
    english_guess = de_gnomeify_sentence(gnomified)
    st.markdown("**Reverse-Translated (guess):**")
    st.markdown(f"<div style='font-size:1.1em'>{english_guess}</div>", unsafe_allow_html=True)

# --- Box 2: Gnome to English ---
st.write("---")
st.write("Or paste some Gnome/Gnlish below to decode back to English:")

gnome_input = st.text_area("Paste Gnome/Goblin text here:", "")

if gnome_input:
    english_decoded = de_gnomeify_sentence(gnome_input)
    st.markdown("**Reverse-Translated:**")
    st.markdown(f"<div style='font-size:1.2em'>{english_decoded}</div>", unsafe_allow_html=True)

