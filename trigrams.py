# In this file the trigrams are generated on the basis of the titanic script(emotions), ghostbusters(buisness and action) and the cure for insomnia(longest script in existence).

# This programme uses 1250mb of RAM-memory
# The programme uses at most 10% of the CPU (Ryzen 5 3600 @ 4.00GHz)

# This in a standard import for regular expressions(regex) built into python
import re

# Trigram dictionaries for different languages
Titanic_EN = {}
Titanic_FR = {}
Titanic_DE = {}
Titanic_NL = {}

GhostBusters_EN = {}
GhostBusters_FR = {}
GhostBusters_DE = {}
GhostBusters_NL = {}

TheCureForInsomnia_EN = {}
TheCureForInsomnia_FR = {}
TheCureForInsomnia_DE = {}
TheCureForInsomnia_NL = {}

# Function to generate trigrams from a given text
def generate_trigrams(text):
    trigrams = {}
    # Split text into words
    # Regex to split text into words, the \b is a word boundary and \w+ is one or more word characters. (for more info: https://docs.python.org/3/library/re.html & https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
    words = re.findall(r'\b\w+\b', text)
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams


# Generate trigrams for each language and script
# Uses the generate_trigrams function to generate trigrams for each script and language
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

with open('scripts/English/TheCureForInsomnia_EN.txt', 'r', encoding='utf-8', errors='replace') as f:
    TheCureForInsomnia_EN = generate_trigrams(f.read())
with open('scripts/French/TheCureForInsomnia_FR.txt', 'r', encoding='utf-8', errors='replace') as f:
    TheCureForInsomnia_FR = generate_trigrams(f.read())
with open('scripts/German/TheCureForInsomnia_DE.txt', 'r', encoding='utf-8', errors='replace') as f:
    TheCureForInsomnia_DE = generate_trigrams(f.read())
with open('scripts/Dutch/TheCureForInsomnia_NL.txt', 'r', encoding='utf-8', errors='replace') as f:
    TheCureForInsomnia_NL = generate_trigrams(f.read())

# Function to detect language based on trigrams and return the used language
def detect_language(input_sentence):
    trigrams = generate_trigrams(input_sentence)

    # Initialize scores for each language and script
    Titanic_EN_score = 0
    Titanic_FR_score = 0
    Titanic_DE_score = 0
    Titanic_NL_score = 0
    GhostBusters_EN_score = 0
    GhostBusters_FR_score = 0
    GhostBusters_DE_score = 0
    GhostBusters_NL_score = 0
    TheCureForInsomnia_EN_score = 0
    TheCureForInsomnia_FR_score = 0
    TheCureForInsomnia_DE_score = 0
    TheCureForInsomnia_NL_score = 0

    # Calculate scores for Titanic, GhostBusters an TheCureForInsomnia in each language
    # English language detection
    for pair in trigrams:
        if pair in Titanic_EN:
            Titanic_EN_score += 1
        if pair in GhostBusters_EN:
            GhostBusters_EN_score += 1
        if pair in TheCureForInsomnia_EN:
            TheCureForInsomnia_EN_score += 1

    # French language detection
    for pair in trigrams:
        if pair in Titanic_FR:
            Titanic_FR_score += 1
        if pair in GhostBusters_FR:
            GhostBusters_FR_score += 1
        if pair in TheCureForInsomnia_FR:
            TheCureForInsomnia_FR_score += 1

    # German language detection
    for pair in trigrams:
        if pair in Titanic_DE:
            Titanic_DE_score += 1
        if pair in GhostBusters_DE:
            GhostBusters_DE_score += 1
        if pair in TheCureForInsomnia_DE:
            TheCureForInsomnia_DE_score += 1

    # Dutch language detection
    for pair in trigrams:
        if pair in Titanic_NL:
            Titanic_NL_score += 1
        if pair in GhostBusters_NL:
            GhostBusters_NL_score += 1
        if pair in TheCureForInsomnia_NL:
            TheCureForInsomnia_NL_score += 1

    # Calculate total scores for each language
    Language_EN_total = Titanic_EN_score + GhostBusters_EN_score + TheCureForInsomnia_EN_score
    Language_FR_total = Titanic_FR_score + GhostBusters_FR_score + TheCureForInsomnia_FR_score
    Language_DE_total = Titanic_DE_score + GhostBusters_DE_score + TheCureForInsomnia_DE_score
    Language_NL_total = Titanic_NL_score + GhostBusters_NL_score + TheCureForInsomnia_NL_score

    print("English score:", Language_EN_total)
    print("French score:", Language_FR_total)
    print("German score:", Language_DE_total)
    print("Dutch score:", Language_NL_total)

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
