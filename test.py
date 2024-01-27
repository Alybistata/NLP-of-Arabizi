import csv

latin_to_arabic = {
    'a': 'ا',
    'b': 'ب',
    'c': 'س',
    'd': 'د',
    'e': 'ع',
    'f': 'ف',
    'g': 'ج',
    'h': 'ه',
    'i': 'ي',
    'j': 'ج',
    'k': 'ك',
    'l': 'ل',
    'm': 'م',
    'n': 'ن',
    'o': 'و',
    'p': 'ب',
    'q': 'ق',
    'r': 'ر',
    's': 'س',
    't': 'ت',
    'u': 'و',
    'v': 'ف',
    'w': 'و',
    'x': 'إكس',
    'y': 'ي',
    'z': 'ز',
}

arabic_to_latin = {v: k for k, v in latin_to_arabic.items()}

def latin_to_arabic_transliteration(text):
    return ''.join(latin_to_arabic.get(char, char) for char in text)

def arabic_to_latin_transliteration(text):
    return ''.join(arabic_to_latin.get(char, char) for char in text)

def search_csv(name, csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['arabic'] == name:
                return row['english']
            elif row['english'] == name:
                return row['arabic']
    return None

# Get input from the user
user_input = input("Enter name: ")

# Determine search direction based on input
search_direction = 'arabic_to_english' if all(char in arabic_to_latin for char in user_input) else 'english_to_arabic'

# Search in the CSV file
result = search_csv(user_input, 'names.csv')

if result:
    print(f'Result for {user_input}: {result}')
else:
    # Use transliteration as a fallback
    if search_direction == 'arabic_to_english':
        transliterated_arabic = latin_to_arabic_transliteration(user_input)
        print(f'Latin to Arabic: {user_input} -> {transliterated_arabic}')
    elif search_direction == 'english_to_arabic':
        transliterated_latin = arabic_to_latin_transliteration(user_input)
        print(f'Arabic to Latin: {user_input} -> {transliterated_latin}')
