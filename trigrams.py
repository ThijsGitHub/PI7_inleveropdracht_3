# This programme detects the language of a given sentence using trigrams of different languages and scripts

# Import regular expressions module, this is a standard module in Python so no need to install it
import re


# Function to generate bigrams for a given text
def generate_bigrams(text):
    bigrams = {}
    words = re.findall(r'\b\w+\b', text) # Find all words in the text using regular expressions(Regex) for more information (on the characters used to make this work) visit https://docs.python.org/3/library/re.html
    for i in range(len(words) - 1): # Looks at the first word and the next word
        pair = (words[i], words[i + 1])
        bigrams.setdefault(pair, 0)
        bigrams[pair] += 1
    return bigrams


# Function to generate trigrams for a given text
def generate_trigrams(text):
    trigrams = {}
    words = re.findall(r'\b\w+\b', text) # Find all words in the text using regular expressions(Regex) for more information (on the characters used to make this work) visit https://docs.python.org/3/library/re.html
    for i in range(len(words) - 2): # Looks at the first word and the next two words
        pair = (words[i], words[i + 1])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


# For this usecase we are using the Titanic, GhostBusters and TheCureForInsomnia scripts in English, French, German and Dutch
# These scripts are used because they are touching on emotional, scientific and philosophical topics. This way it possible to recognize a great deal of words in different languages.

# Function to generate trigrams for a given language and script
# For bigrams:
def generate_bigrams_for_language(script_path, language_dict):
    with open(script_path, 'r', encoding='utf-8', errors='replace') as f: # Open script file with UTF-8 encoding and replace errors because of invalid characters caused during translation of the scripts
        language_dict.update(generate_bigrams(f.read()))

# For trigrams:
def generate_trigrams_for_language(script_path, language_dict):
    with open(script_path, 'r', encoding='utf-8', errors='replace') as f: # Open script file with UTF-8 encoding and replace errors because of invalid characters caused during translation of the scripts
        language_dict.update(generate_trigrams(f.read()))


# Function to detect language of a given sentence
# For bigrams:
def detect_language_bi(input_sentence, language_dicts):
    bigrams = generate_bigrams(input_sentence)
    scores = {language: sum(1 for pair in bigrams if pair in language_dict) for language, language_dict in language_dicts.items()}
    language = max(scores, key=scores.get)
    return scores, language

# For trigrams:
def detect_language_tri(input_sentence, language_dicts):
    trigrams = generate_trigrams(input_sentence)
    scores = {language: sum(1 for pair in trigrams if pair in language_dict) for language, language_dict in language_dicts.items()}
    language = max(scores, key=scores.get)
    return scores, language


# Bi- and Trigram dictionaries for different languages and scripts
languagesB = {
    'English': {},
    'French': {},
    'German': {},
    'Dutch': {}
}

languagesT = languagesB.copy()

# Generate bigrams for each script in each language
for language, language_dict in languagesB.items():
    for script in ['Titanic', 'GhostBusters', 'TheCureForInsomnia', 'WolfOfWallStreet']:
        script_path = f'scripts/{language}/{script}_{language}.txt'
        generate_bigrams_for_language(script_path, language_dict)

# Generate trigrams for each script in each language
for language, language_dict in languagesT.items():
    for script in ['Titanic', 'GhostBusters', 'TheCureForInsomnia', 'WolfOfWallStreet']:
        script_path = f'scripts/{language}/{script}_{language}.txt'
        generate_trigrams_for_language(script_path, language_dict)


# Ask user for input sentence
input_sentence = input("Enter a sentence: ")


# Detect language of input sentence using bigrams
scores_bi, language_bi = detect_language_bi(input_sentence, languagesB)
if sum(scores_bi.values()) == 0:
    print("There are no points awarded according to bi-grams...")
else:
    print("The input sentence is written in", language_bi, "according to the bigrams.")

# Detect language of input sentence using trigrams
scores_tri, language_tri = detect_language_tri(input_sentence, languagesT)
if sum(scores_tri.values()) == 0:
    print("There are no points awarded according to tri-grams...")
else:
    print("The input sentence is written in", language_tri, "according to the trigrams.")


total_score = sum(scores_bi.values())
if total_score == 0:
        print("There is no detected language according to bi-grams...")
else:
    print("Scores per language (bi-grams):")
    for lang, score in scores_bi.items():
        percentage = (score / total_score) * 100
        print(lang, "{:.2f}%".format(percentage), "(score:", score, ")")

total_score = sum(scores_tri.values())
if total_score == 0:
        print("There is no detected language according to tri-grams...")
else:
    print("Scores per language (tri-grams):")
    for lang, score in scores_tri.items():
        percentage = (score / total_score) * 100
        
        print(lang, "{:.2f}%".format(percentage), "(score:", score, ")")
