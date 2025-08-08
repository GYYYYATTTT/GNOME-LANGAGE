#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MEGA DICTIONARY: English to Gnome
EN_TO_GNOME = {
    # Greetings, phrases
    "hello": "glorbik", "hi": "gribby", "good morning": "blorn morzn", "good night": "blorn nizz",
    "goodbye": "blornib", "see you soon": "glorr tu bliz", "how are you": "fropp tu", "i'm fine": "ik blonzy",
    "what's up": "vobb ubb", "cheers": "bruzzik", "welcome": "blonkam",
    # People & professions
    "person": "blonson", "man": "grim", "woman": "glimma", "child": "sniblet", "friend": "blonfrib",
    "enemy": "skraggfrib", "teacher": "blontraik", "student": "graddik", "worker": "blibworr",
    "trader": "trinnokar", "miner": "blonmynn", "developer": "kodblib", "artist": "blonart", "singer": "blonsingk",
    "leader": "chiefnik",
    # Emotions, states
    "proud": "pronnik", "jealous": "jellik", "nervous": "nervik", "bored": "snorby", "relaxed": "laxxik",
    "scared": "skerrik", "surprised": "surprik", "confused": "confoozik", "embarrassed": "blushik",
    "patient": "pashnik", "stubborn": "stubblik", "shy": "shynik", "happy": "zibble", "sad": "glumby",
    "angry": "blurg", "excited": "zipzip", "tired": "flopty", "hungry": "ploggy", "thirsty": "glibby",
    "lost": "wibby", "busy": "gribby",
    # Science & tech
    "science": "scibbl", "math": "matnik", "chemistry": "chemnik", "physics": "fiznik", "computer": "compik",
    "software": "softwik", "hardware": "hardwik", "robot": "robblik", "internet": "netbik", "email": "emibb",
    "phone": "fonnik", "battery": "battik", "code": "kodnik", "program": "progbrik", "data": "datnik", "virus": "viruzz",
    # Crypto, business, money
    "coin": "groink", "coins": "groinkzz", "wallet": "blimbor", "blockchain": "kladdock", "token": "flarn",
    "bitcoin": "brizzcoin", "ethereum": "ethergrok", "solana": "solgrib", "pump": "yipzz", "dump": "flopzz",
    "liquidity": "glibber", "trade": "trinnock", "buy": "boik", "sell": "sekk", "price": "prilz", "bullish": "glibbozz",
    "bearish": "fluppozz", "scam": "skragg", "rugpull": "rugblok", "whale": "bloopk", "moon": "blupk",
    "NFT": "nifft", "DEX": "zexblib", "meme coin": "plizzle", "chart": "chort", "market": "merkad", "money": "munnik",
    "salary": "sallik", "tax": "taxik", "bill": "billik", "pay": "paynik", "bank": "bankik", "value": "valyik",
    "debt": "debbik", "investment": "inviblik", "profit": "profik", "loss": "loosik",
    # Education & school
    "school": "skolnik", "class": "klassik", "lesson": "lessnik", "book": "bukkik", "homework": "homworrik",
    "exam": "egzammik", "question": "questnik", "answer": "ansbrik",
    # Sports
    "sport": "sportik", "game": "gamik", "player": "plarnik", "team": "teemik", "ball": "ballik", "soccer": "fuballik",
    "basketball": "hoopnik", "tennis": "tennik", "swim": "swimik", "run": "frizz", "jump": "jumplik", "win": "glibber",
    "lose": "loosik",
    # Family & relationships
    "family": "famblik", "mother": "momnik", "father": "fadnik", "sister": "sistik", "brother": "brornik",
    "son": "sonnib", "daughter": "dautnik", "uncle": "unkik", "aunt": "auntik", "cousin": "kuznik", "partner": "partnik",
    "baby": "babblik",
    # Body, medical
    "head": "hednib", "face": "faznik", "eye": "eynik", "nose": "noznik", "mouth": "mouzik", "ear": "earnik",
    "arm": "armnik", "hand": "handik", "leg": "legnik", "foot": "futnik", "heart": "hartik", "blood": "blodnik",
    "doctor": "docnik", "nurse": "nursik", "hospital": "hospik", "sick": "siknik", "medicine": "medzik", "pain": "paynik",
    "wound": "wunnik",
    # Places & transport
    "car": "clarn", "bus": "buzzik", "train": "tronn", "plane": "blaynik", "bike": "blonnik", "taxi": "taxnik",
    "airport": "airpork", "station": "statnik", "port": "portnik", "bridge": "bridjik", "shop": "shoppik",
    "park": "parnik", "cinema": "movik", "theater": "theatrik", "museum": "musnik", "library": "librik",
    "restaurant": "restik", "bar": "pubbik", "street": "strib", "square": "squarik", "church": "chuchik",
    "building": "buildik",
    # Nature, weather, directions
    "sun": "solbik", "moon": "blupk", "star": "starnik", "sky": "sklarn", "cloud": "cludd", "rain": "rainnik",
    "snow": "snorflik", "wind": "whifnik", "mountain": "montik", "river": "ribblik", "forest": "fornik",
    "flower": "flornik", "tree": "grobble", "leaf": "leevnik", "grass": "gribbl", "fire": "fyrnik", "earth": "urthik",
    "stone": "snigg", "sand": "sandik", "north": "nornik", "south": "sornik", "east": "eaznik", "west": "weznik",
    "ocean": "oshnik", "sea": "seanik", "lake": "laknik", "valley": "vallik", "island": "islnik", "desert": "desnik",
    # Food & drink
    "water": "plibnob", "coffee": "kaffik", "tea": "tezz", "beer": "bruzz", "bread": "blenn", "cheese": "chebble",
    "meat": "snarn", "soup": "soopple", "fruit": "flom", "vegetable": "vobble", "apple": "applik", "banana": "bananik",
    "orange": "oranjik", "grape": "grapnik", "potato": "potanik", "tomato": "tomatik", "onion": "onnik",
    "carrot": "carik", "lettuce": "lettik", "chicken": "chikkik", "beef": "beefnik", "pork": "porkik", "egg": "eggnik",
    "cake": "cakik", "chocolate": "chokkik", "salt": "salkik", "pepper": "peppik",
    # Animals
    "animal": "blonmal", "dog": "dawgik", "cat": "katnik", "bird": "birbik", "fish": "blonfin", "mouse": "mausnik",
    "cow": "cownik", "horse": "hossik", "bear": "beryk", "wolf": "wolnik", "rabbit": "rabbik", "fox": "foxnik",
    "snake": "snaknik", "dragon": "draggik",
    # Entertainment & media
    "music": "muzik", "song": "songnik", "sing": "singk", "dance": "dansik", "movie": "movik", "actor": "aktorik",
    "television": "telvnik", "video": "vidik", "photo": "fotnik", "picture": "pictik", "art": "blonart", "draw": "drawnik",
    "paint": "paintik", "read": "rednik",
    # Fantasy
    "wizard": "wizzik", "witch": "witchnik", "fairy": "fairnik", "dwarf": "dworvik", "elf": "elfnik", "goblin": "gobblik",
    "troll": "trollik", "spell": "spellik", "potion": "potik", "sword": "swordik", "shield": "shielnik",
    "castle": "caslik", "dungeon": "dungik", "quest": "questnik", "treasure": "treazik",
    # Slang & crypto memes
    "gm": "gmnorzn", "gn": "gnnizz", "wagmi": "wagmizz", "ngmi": "ngmizz", "fomo": "fommik", "fud": "fuddik",
    "lfg": "luffgik", "rekt": "rektik", "shill": "shillik", "degen": "degenik", "snipe": "snipnik", "floor price": "florpilz",
    "ath": "athnik", "bag holder": "baghldik", "dip": "dippik",
    # Time, numbers, colors, months
    "day": "dozz", "night": "nizz", "morning": "morzn", "evening": "evvyn", "hour": "hourb", "minute": "minnit",
    "second": "sekkond", "week": "wekk", "month": "montek", "year": "yarr",
    "january": "janik", "february": "febbik", "march": "marnik", "april": "aprik", "may": "maynik", "june": "junnik",
    "july": "jullik", "august": "auggik", "september": "seppik", "october": "octik", "november": "novik", "december": "decik",
    "monday": "modik", "tuesday": "tudik", "wednesday": "wednik", "thursday": "thurnik", "friday": "fridik", "saturday": "satnik", "sunday": "sundik",
    "zero": "zerro", "one": "onib", "two": "doob", "three": "trebb", "four": "flubb", "five": "vibbl", "six": "sizz", "seven": "zevv", "eight": "aitt", "nine": "nizz", "ten": "tennib",
    "eleven": "elvnik", "twelve": "twelbik", "thirteen": "tirtnik", "twenty": "twenib", "thirty": "thirtik", "forty": "fortik", "fifty": "fiftik", "hundred": "hundrik", "thousand": "thauzik",
    # Colors
    "red": "reddik", "orange": "ornjik", "yellow": "yelnik", "green": "grennik", "blue": "blunik", "purple": "purplik",
    "pink": "pinkik", "black": "blakkik", "white": "wytik", "brown": "brunnik", "gray": "graynik",
    # Commands, misc
    "stop": "skriff", "go": "snorb", "come": "kommik", "wait": "waibb", "jump": "jumplik", "sit": "sittik", "stand": "standik",
    "start": "starnik", "open": "opennik", "close": "closik", "look": "looknik", "listen": "lisnik", "thing": "thingnik",
    "stuff": "stufnik", "place": "plasek", "reason": "reaznik", "secret": "secretnik", "magic": "magik", "legend": "legnik", "dream": "dreemik",
    # Function words
    "the": "blib", "a": "blib", "and": "gnar", "to": "", "is": "", "are": "", "of": "", "on": "", "in": "", "with": "",
    "i": "ik", "you": "tu", "we": "wib", "they": "drim", "he": "gruk", "she": "gruk", "it": "gruk", "my": "mik", "your": "turk",
    "his": "hisk", "her": "hirk", "their": "thirk", "our": "wurk", "this": "thiz", "that": "thatz", "for": "", "at": "",
    "from": "", "by": "", "not": "snarf", "no": "snarf", "yes": "blorf", "please": "plizz", "thank you": "blunty", "thanks": "blunty", "sorry": "flintzy", "help": "gront", "who": "kloo", "what": "vobb", "when": "glimm", "where": "zrun", "why": "glurff", "how": "fropp",

    "house": "domnik",
    "apartment": "aparnik",
    "room": "runnik",
    "bed": "bednik",
    "table": "tablik",
    "chair": "charnik",
    "window": "vindik",
    "door": "dorrik",
    "floor": "flornik",
    "wall": "wallik",
    "roof": "rofnik",
    "kitchen": "kitchnik",
    "bathroom": "bathnik",
    "toilet": "toilnik",
    "shower": "showernik",
    "couch": "couchik",
    "lamp": "lampik",
    "light": "laitnik",
    "mirror": "mirrik",
    "clothes": "klothzz",
    "shirt": "shertik",
    "pants": "pantzz",
    "shoes": "shuznik",
    "sock": "sockik",
    "coat": "kotnik",
    "dress": "dresnik",
    "hat": "hatnik",
    "bag": "bagnik",
    "key": "keeyik",
    "phone": "fonnik",
    "computer": "compik",
    "mouse (device)": "devmausnik",
    "screen": "skrenik",
    "cable": "kabelik",
    "remote": "remotik",

 "fast": "yipnik",
    "slow": "drounik",
    "old": "oldnik",
    "new": "nywik",
    "young": "yunggik",
    "strong": "stronkik",
    "weak": "wiknik",
    "clean": "klinnek",
    "dirty": "durtnik",
    "rich": "ricnik",
    "poor": "poornik",
    "hard": "hardik",
    "easy": "easik",
    "happy": "zibble",
    "sad": "glumby",
    "funny": "funik",
    "serious": "sernik",
    "loud": "loudnik",
    "quiet": "quiynik",
    "long": "lonnik",
    "short": "shortik",
    "full": "fullik",
    "empty": "emptik", 

  "rice": "risnik",
    "pasta": "pastik",
    "pizza": "pizzik",
    "sushi": "sushnik",
    "hamburger": "hambrik",
    "sandwich": "sandvik",
    "salad": "saladik",
    "milk": "milnik",
    "juice": "juicik",
    "wine": "winik",
    "water": "plibnob",
    "ice": "aisnik",
    "butter": "buttrik",
    "oil": "oylnik",
    "sugar": "sugrik",
    "honey": "honik",
    "salt": "salkik",
    "pepper": "peppik",

 "tree": "grobble",
    "bush": "bushik",
    "flower": "flornik",
    "leaf": "leevnik",
    "grass": "gribbl",
    "rock": "snigg",
    "mountain": "montik",
    "hill": "hillik",
    "field": "fieldik",
    "river": "ribblik",
    "lake": "laknik",
    "pond": "pondik",
    "sea": "seanik",
    "beach": "beechik",
    "desert": "desnik",
    "island": "islnik",
"ticket": "tickik",
    "passport": "passnik",
    "luggage": "luggik",
    "map": "mapnik",
    "travel": "travnik",
    "holiday": "holidik",
    "trip": "tripnik",
    "journey": "jurnik",
    "visit": "visnik",
    "arrive": "arrivnik",
    "leave": "leavik",
    "wifi": "wifik",
    "username": "usermik",
    "password": "passwik",
    "account": "accounik",
    "login": "logik",
    "logout": "logautik",
    "website": "websik",
    "app": "appnik",
    "download": "downik",
    "upload": "upnik",
    "link": "linkik",
    "hashtag": "hashnik",
    "gas": "gazzik",
    "yield": "yielnik",
    "farm": "farmik",
    "stake": "steykik",
    "mint": "mintik",
    "swap": "swappik",
    "bridge": "brijik",
    "governance": "govnik",
    "dao": "daonik",
    "wallet": "blimbor",
    "seed phrase": "seedfrik",
    "burn": "burnik",
    "claim": "claimik",
    "snapshot": "snapik",
    "vault": "vaultik",
    "tokenomics": "toknomik",
    "angry": "blurg",
    "afraid": "afradik",
    "ashamed": "ashamnik",
    "excited": "zipzip",
    "curious": "qurinik",
    "brave": "bravik",
    "hopeful": "hopnik",
    "calm": "calmik"

}


GNOME_TO_EN = {v: k for k, v in EN_TO_GNOME.items()}

def english_to_gnome(phrase):
    # Handle punctuation
    import re
    phrase = re.sub(r"[.,!?]", "", phrase)
    words = phrase.lower().split()
    gnome_words = []
    skip_next = False
    for i, w in enumerate(words):
        if skip_next:
            skip_next = False
            continue
        # Check for 2-word (or more) phrases, longest match
        found = False
        for n in range(3, 0, -1):  # up to 3-word phrases
            if i + n <= len(words):
                phrase_candidate = " ".join(words[i:i+n])
                if phrase_candidate in EN_TO_GNOME:
                    gnome_words.append(EN_TO_GNOME[phrase_candidate])
                    skip_next = n - 1
                    found = True
                    break
        if not found:
            gnome_words.append(EN_TO_GNOME.get(w, w + "zz"))
    return " ".join(gnome_words)

def gnome_to_english(phrase):
    words = phrase.replace("znok?", "").split()
    english_words = []
    for w in words:
        base_w = w.replace("zz", "")
        if w in GNOME_TO_EN:
            english_words.append(GNOME_TO_EN[w])
        elif base_w in GNOME_TO_EN:
            english_words.append(GNOME_TO_EN[base_w])
        else:
            english_words.append(w)
    if "znok?" in phrase:
        english_words.append("?")
    return " ".join(english_words).capitalize()

# ---- Example Usage ----

# English to Gnome
print(english_to_gnome("pump that shit"))

# Gnome to English
print(gnome_to_english("wizzik glibb blib magik potik prezz blib questnik"))


# In[ ]:





# In[3]:


import streamlit as st

# ---- Paste your EN_TO_GNOME dictionary here ----
EN_TO_GNOME = {
    "hello": "glorbik", "goodbye": "blornib", "friend": "blonfrib", "the": "blib", "pump": "yipzz",
    "wizard": "wizzik", "magic": "magik", "potion": "potik", "quest": "questnik", "moon": "blupk",
    "bitcoin": "brizzcoin", "meme": "plizzle", "coin": "groink", "and": "gnar", "to": "",
    "i": "ik", "am": "", "you": "tu", "eat": "yook", "pizza": "pizzik", "in": "", "on": "",
    "mountain": "montik", "good": "blorn", "night": "nizz", "morning": "morzn", "yes": "blorf", "no": "snarf",
    # ...add more as needed!
}

def english_to_gnome(phrase):
    import re
    phrase = re.sub(r"[.,!?]", "", phrase)
    words = phrase.lower().split()
    gnome_words = []
    skip_next = False
    for i, w in enumerate(words):
        if skip_next:
            skip_next = False
            continue
        if i < len(words) - 1 and f"{w} {words[i+1]}" in EN_TO_GNOME:
            gnome_words.append(EN_TO_GNOME[f"{w} {words[i+1]}"])
            skip_next = True
        else:
            gnome_words.append(EN_TO_GNOME.get(w, w + "zz"))
    return " ".join(gnome_words)

def to_fraktur(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    fraktur = [
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
    ]
    mapping = {c: f for c, f in zip(normal, fraktur[0] + fraktur[1])}
    return ''.join(mapping.get(ch, ch) for ch in text)

# --- Streamlit User Interface ---
st.title("Gnome Translator 🧙‍♂️")
st.write("Type English below and see your Gnome translation in 𝔉𝔯𝔞𝔨𝔱𝔲𝔯 style!")

text = st.text_area("Enter English text:", "")

if text:
    gnome = english_to_gnome(text)
    st.markdown("**Gnome Translation:**")
    st.markdown(f"<div style='font-size:2em'>{to_fraktur(gnome)}</div>", unsafe_allow_html=True)


# In[ ]:




