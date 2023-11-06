import time
import re
from tabulate import tabulate # This package is used to print the scores in a table, not necessary for the language detection itself

# Function to generate n-grams for a given text
def generate_ngrams(text, n):
    ngrams = {}
    words = re.findall(r'\b\w+\b', text)
    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i + n])
        ngrams.setdefault(ngram, 0)
        ngrams[ngram] += 1
    return ngrams

# For this usecase we are using the Titanic, GhostBusters and TheCureForInsomnia scripts in English, French, German and Dutch
# These scripts are used because they are touching on emotional, scientific and philosophical topics. This way it possible to recognize a great deal of words in different languages.
# Function to generate n-grams for a given language and script
def generate_ngrams_for_language(script_path, language_dict, n):
    with open(script_path, 'r', encoding='utf-8', errors='replace') as f:
        ngrams = generate_ngrams(f.read(), n)
        language_dict.update(ngrams)
        return language_dict

# Function to detect language of a given sentence
def detect_language(input_sentence, language_dicts, n):
    ngrams = generate_ngrams(input_sentence, n)
    scores = {language: sum(1 for ngram in ngrams if ngram in language_dict) for language, language_dict in language_dicts.items()}
    language = max(scores, key=scores.get)
    return scores, language

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
            table.append([lang, "{:.1f}%".format(percentage), score])
        print(tabulate(table, headers=["Language", "Percentage", "Score"]))

# Initialize dictionaries for different languages and scripts
languages = {
    'English': {},
    'French': {},
    'German': {},
    'Dutch': {},
    'Italian': {},
    'Spanish': {}
}

# Generate n-grams for each script in each language
for language, language_dict in languages.items():
    for script in ['Titanic', 'GhostBusters', 'TheCureForInsomnia', 'WolfOfWallStreet']:
        script_path = f'scripts/{language}/{script}_{language}.txt'
        language_dict = generate_ngrams_for_language(script_path, language_dict, 2)
        language_dict = generate_ngrams_for_language(script_path, language_dict, 3)

input_sentence = input("Enter a sentence: ")

# Detect language of the input sentence using bigrams and trigrams
scores_bi, language_bi = detect_language(input_sentence, languages, 2)
scores_tri, language_tri = detect_language(input_sentence, languages, 3)

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

# Function to calculate the accuracy of language detection
def calculate_accuracy(test_set, language_dicts, n):
    correct_count = 0

    for sentence, true_language in test_set:
        _, detected_language = detect_language(sentence, language_dicts, n)

        if detected_language == true_language:
            correct_count += 1

    accuracy = (correct_count / len(test_set)) * 100
    return accuracy

# Function to measure the processing time of language detection
def measure_processing_time(sentence, language_dicts, n):
    start_time = time.time()
    _, _ = detect_language(sentence, language_dicts, n)
    end_time = time.time()
    processing_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    return processing_time_ms

# Test set with sentences in different languages
test_set = [
    ("This is an English sentence, and it surely is quite marvelous.", "English"),
    ("C'est une phrase anglaise, et elle est sûrement assez merveilleuse.", "French"),
    ("Dies ist ein englischer Satz, und er ist sicherlich ganz wunderbar.", "German"),
    ("Dit is een Engelse zin, en het is beslist heel wonderbaarlijk.", "Dutch"),
    ("Questa è una frase inglese e sicuramente è davvero meravigliosa.", "Italian"),
    ("Esta es una frase en inglés y seguramente es bastante maravillosa.", "Spanish"),
]

# Measure the processing time for a short sentence
short_sentence = "This is a very, very short sentence."
processing_time_short_bi = measure_processing_time(short_sentence, languages, 2)
processing_time_short_tri = measure_processing_time(short_sentence, languages, 3)

# Measure the processing time for a long sentence
long_sentence = 'long_sentence.txt'
processing_time_long_bi = measure_processing_time(long_sentence, languages, 2)
processing_time_long_tri = measure_processing_time(long_sentence, languages, 3)

# Calculate the accuracy of language detection
accuracy_bi = calculate_accuracy(test_set, languages, 2)
accuracy_tri = calculate_accuracy(test_set, languages, 3)

# Show the results
print(f"Accuracy with bigrams: {accuracy_bi:.2f}%")
print(f"Accuracy with trigrams: {accuracy_tri:.2f}%")

print(f"Process time for a short sentance, using bigrams: {processing_time_short_bi:.2f} ms")
print(f"Process time for a short sentance, using trigrams: {processing_time_short_tri:.2f} ms")

print(f"Process time for a long sentance, using bigrams: {processing_time_long_bi:.2f} ms")
print(f"Process time for a long sentance, using trigrams: {processing_time_long_tri:.2f} ms")
