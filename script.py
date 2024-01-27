import csv
import farasa

def load_transliteration_dictionary(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) == 2:
                arabic_name, latin_name = row
                dictionary[arabic_name] = latin_name
    return dictionary

def transliterate_name(name, dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        # Transliterate using farasa transliteration
        return farasa.transliterate(name)

def main():
    csv_file_path = 'names.csv'
    transliteration_dictionary = load_transliteration_dictionary(csv_file_path)

    while True:
        input_name = input("Enter a name to transliterate (or 'exit' to quit): ")
        if input_name.lower() == 'exit':
            break

        # Check if the name is in Arabic or Latin
        is_arabic = all('\u0600' <= char <= '\u06FF' for char in input_name)
        
        if is_arabic:
            transliterated_name = transliterate_name(input_name, transliteration_dictionary)
            print(f"Transliterated to Latin: {transliterated_name}")
        else:
            reversed_dictionary = {v: k for k, v in transliteration_dictionary.items()}
            transliterated_name = transliterate_name(input_name, reversed_dictionary)
            print(f"Transliterated to Arabic: {transliterated_name}")

if __name__ == "__main__":
    main()
