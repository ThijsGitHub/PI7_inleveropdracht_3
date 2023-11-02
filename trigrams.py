# This programme detects the language of a given sentence using trigrams of different languages and scripts

# Import regular expressions module, this is a standard module in Python so no need to install it
import re

# Function to generate trigrams for a given text
def generate_trigrams(text):
    trigrams = {}
    words = re.findall(r'\b\w+\b', text) # Find all words in the text using regular expressions(Regex) for more information (on the characters used to make this work) visit https://docs.python.org/3/library/re.html
    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams

# Function to generate trigrams for a given language and script
def generate_trigrams_for_language(script_path, language_dict):
    with open(script_path, 'r', encoding='utf-8', errors='replace') as f: # Open script file with UTF-8 encoding and replace errors because of invalid characters caused during translation of the scripts
        language_dict.update(generate_trigrams(f.read()))

def detect_language(input_sentence, language_dicts):
    trigrams = generate_trigrams(input_sentence)
    scores = {language: sum(1 for pair in trigrams if pair in language_dict) for language, language_dict in language_dicts.items()}
    language = max(scores, key=scores.get)
    return language

# Trigram dictionaries for different languages and scripts
languages = {
    'English': {},
    'French': {},
    'German': {},
    'Dutch': {},
}

# Generate trigrams for each language and script
for language, language_dict in languages.items():
    for script in ['Titanic', 'GhostBusters', 'TheCureForInsomnia']:
        script_path = f'scripts/{language}/{script}_{language}.txt'
        generate_trigrams_for_language(script_path, language_dict)

# Ask user for input sentence
input_sentence = input("Enter a sentence: ")

# Detect language of input sentence
language = detect_language(input_sentence, languages)
print("The input sentence is written in", language)
