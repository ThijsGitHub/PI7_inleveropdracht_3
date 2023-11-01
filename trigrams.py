import re
import random

# Trigram dictionaries for different languages
Titanic_EN = {}
Titanic_FR = {}
Titanic_DE = {}
Titanic_NL = {}

GhostBusters_EN = {}
GhostBusters_FR = {}
GhostBusters_DE = {}
GhostBusters_NL = {}

# Function to generate trigrams from a given text
def generate_trigrams(text):
    trigrams = {}
    words = re.findall(r'\b\w+\b', text)
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

# Generate trigrams for each language
with open('scripts/English/Titanic_EN.txt', 'r', encoding='utf-8', errors='replace') as f:
    Titanic_EN = generate_trigrams(f.read())
with open('scripts/French/Titanic_FR.txt', 'r', encoding='utf-8', errors='replace') as f:
    Titanic_FR = generate_trigrams(f.read())
with open('scripts/German/Titanic_DE.txt', 'r', encoding='utf-8', errors='replace') as f:
    Titanic_DE = generate_trigrams(f.read())
with open('scripts/Dutch/Titanic_NL.txt', 'r', encoding='utf-8', errors='replace') as f:
    Titanic_NL = generate_trigrams(f.read())

with open('scripts/English/GhostBusters_EN.txt', 'r', encoding='utf-8', errors='replace') as f:
    GhostBusters_EN = generate_trigrams(f.read())
with open('scripts/French/GhostBusters_FR.txt', 'r', encoding='utf-8', errors='replace') as f:
    GhostBusters_FR = generate_trigrams(f.read())
with open('scripts/German/GhostBusters_DE.txt', 'r', encoding='utf-8', errors='replace') as f:
    GhostBusters_DE = generate_trigrams(f.read())
with open('scripts/Dutch/GhostBusters_NL.txt', 'r', encoding='utf-8', errors='replace') as f:
    GhostBusters_NL = generate_trigrams(f.read())

# Function to detect language based on trigrams and return the used language
def detect_language(input_sentence):
    trigrams = generate_trigrams(input_sentence)
    Titanic_EN_score = 0
    Titanic_FR_score = 0
    Titanic_DE_score = 0
    Titanic_NL_score = 0
    GhostBusters_EN_score = 0
    GhostBusters_FR_score = 0
    GhostBusters_DE_score = 0
    GhostBusters_NL_score = 0

    # Calculate scores for English Titanic and GhostBusters
    for pair in Titanic_EN:
        if pair in trigrams:
            Titanic_EN_score += len(Titanic_EN[pair])
    for pair in GhostBusters_EN:
        if pair in trigrams:
            Titanic_EN_score += len(GhostBusters_EN[pair])

    # Calculate scores for French Titanic and GhostBusters
    for pair in Titanic_FR:
        if pair in trigrams:
            Titanic_FR_score += len(Titanic_FR[pair])
    for pair in GhostBusters_FR:
        if pair in trigrams:
            Titanic_FR_score += len(GhostBusters_FR[pair])

    # Calculate scores for German Titanic and GhostBusters
    for pair in Titanic_DE:
        if pair in trigrams:
            Titanic_DE_score += len(Titanic_DE[pair])
    for pair in GhostBusters_DE:
        if pair in trigrams:
            Titanic_DE_score += len(GhostBusters_DE[pair])

    # Calculate scores for Dutch Titanic and GhostBusters
    for pair in Titanic_NL:
        if pair in trigrams:
            Titanic_NL_score += len(Titanic_NL[pair])
    for pair in GhostBusters_NL:
        if pair in trigrams:
            Titanic_NL_score += len(GhostBusters_NL[pair])

    # Calculate total scores for each language
    Language_EN_total = Titanic_EN_score + GhostBusters_EN_score
    Language_FR_total = Titanic_FR_score + GhostBusters_FR_score
    Language_DE_total = Titanic_DE_score + GhostBusters_DE_score
    Language_NL_total = Titanic_NL_score + GhostBusters_NL_score

    # Return language with highest score
    if Language_EN_total > Language_FR_total and Language_EN_total > Language_DE_total and Language_EN_total > Language_NL_total:
        return "het Engels"
    elif Language_FR_total > Language_EN_total and Language_FR_total > Language_DE_total and Language_FR_total > Language_NL_total:
        return "het Frans"
    elif Language_DE_total > Language_EN_total and Language_DE_total > Language_FR_total and Language_DE_total > Language_NL_total:
        return "het Duits"
    elif Language_NL_total > Language_EN_total and Language_NL_total > Language_FR_total and Language_NL_total > Language_DE_total:
        return "het Nederlands"
    else:
        return "een onbekende taal"

# Ask user for input sentence
input_sentence = input("Voer een zin in: ")

# Detect language of input sentence
language = detect_language(input_sentence)
print("De ingevoerde zin is geschreven in", language)
