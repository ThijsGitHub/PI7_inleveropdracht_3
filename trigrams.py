# This programme detects 1 of 6 languages of a given sentence using trigrams of different languages and movie scripts

# Import tabulate module to print the scores in a table, this is not a standard module in Python so you need to install it first
from tabulate import tabulate

# Import regular expressions module, this is a standard module in Python so no need to install it
import re

# Function to generate bigrams for a given text
def generate_ngrams(text, n):
    ngrams = {}
    words = re.findall(r'\b\w+\b', text) # Find all words in the text using regular expressions(Regex) for more information (on the characters used to make this work) visit https://docs.python.org/3/library/re.html and https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/
    for i in range(len(words) - n + 1): # Looks at the words in the text and creates a tuple of n words (n being 2 for bigrams and 3 for trigrams)
        ngram = tuple(words[i:i + n])
        ngrams.setdefault(ngram, 0)
        ngrams[ngram] += 1
    return ngrams

# For this usecase we are using the Titanic, GhostBusters and TheCureForInsomnia scripts in English, French, German and Dutch
# These scripts are used because they are touching on emotional, scientific and philosophical topics. This way it possible to recognize a great deal of words in different languages. 

# Function to generate trigrams for a given language and script
def generate_ngrams_for_language(script_path, language_dict, n):
    with open(script_path, 'r', encoding='utf-8', errors='replace') as f:
        ngrams = generate_ngrams(f.read(), n)
        language_dict.update(ngrams)  # Update the language_dict with ngrams
        return language_dict  # Return the updated language_dict

# Function to detect language of a given sentence
def detect_language(input_sentence, language_dicts, n):
    ngrams = generate_ngrams(input_sentence, n)
    scores = {language: sum(1 for ngram in ngrams if ngram in language_dict) for language, language_dict in language_dicts.items()}
    language = max(scores, key=scores.get)
    return scores, language

# Dictionaries for different languages and scripts
languages = {
    'English': {},
    'French': {},
    'German': {},
    'Dutch': {},
    'Italian': {},
    'Spanish': {}
}

# Generate bigrams and trigrams for each script in each language
for language, language_dict in languages.items():
    for script in ['Titanic', 'GhostBusters', 'TheCureForInsomnia', 'WolfOfWallStreet']:
        script_path = f'scripts/{language}/{script}_{language}.txt' # Path to the scripts using the languages dictionary to get the path
        generate_ngrams_for_language(script_path, language_dict, 2)  # n=2 for bigrams
        language_dict = generate_ngrams_for_language(script_path, language_dict, 3)  # n=3 for trigrams

input_sentence = input("Enter a sentence: ")

# Detect language of the input sentence using bigrams and trigrams
scores_bi, language_bi = detect_language(input_sentence, languages, 2)
scores_tri, language_tri = detect_language(input_sentence, languages, 3)

# Function to print the scores in a table
def print_scores(scores, language, n):
    total_score = sum(scores.values())
    if total_score == 0:
        print(f"There is no detected language according to {n}-grams...")
    else:
        print(f"Scores per language ({n}-grams):")
        table = []
        for lang, score in scores.items():
            percentage = (score / total_score) * 100
            table.append([lang, "{:.2f}%".format(percentage), score])
        print(tabulate(table, headers=["Language", "Percentage", "Score"]))

if sum(scores_bi.values()) == 0:
    print("There are no detections according to bigrams...")
else:
    print(f"The input sentence is written in {language_bi} according to the bigrams.")
    print_scores(scores_bi, language_bi, 2)

if sum(scores_tri.values()) == 0:
    print("There are no detections according to trigrams...")
else:
    print(f"The input sentence is written in {language_tri} according to the trigrams.")
    print_scores(scores_tri, language_tri, 3)
