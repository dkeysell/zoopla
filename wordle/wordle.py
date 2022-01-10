import requests
import json


def calculate_permutations(config, words, word, alphabet_index):
    if config['max_permutations'] == len(words):
        return words
    if len(word) == config['length_of_word']:
        for valid_letter in config['valid_letters']:
            if valid_letter['letter'] not in word:
                return
        words.append(word)
        return words
    while alphabet_index < len(config['alphabet']):
        letter = config['alphabet'][alphabet_index]
        valid_position = True
        word_index = len(word)
        for valid_letter in config['valid_letters']:
            if valid_letter['letter'] == letter:
                for invalid_position in valid_letter['invalid_positions']:
                    if word_index == invalid_position:
                        valid_position = False
                        break
            elif word_index in valid_letter['valid_positions']:
                valid_position = False
                break
        if valid_position:
            word = word + letter
            calculate_permutations(config, words, word, 0)
            word = word[:-1]
        alphabet_index = alphabet_index + 1
    return words


def initial_alphabet(config):
    filtered_alphabet = ''
    for char in config['alphabet']:
        if char not in config['invalid_letters']:
            filtered_alphabet = filtered_alphabet + char
    config['alphabet'] = filtered_alphabet
    return config


def find_word():
    with open('../resources/wordle/config.json') as config_file:
        config = json.loads(config_file.read())
    config = initial_alphabet(config)
    words = calculate_permutations(config, [], '', 0)

    check_word(config['payload_start'], words, config['payload_end'], config)


def check_word(payload_start, words, payload_end, config):
    words_string = " ".join(words)
    url = "https://jspell-checker.p.rapidapi.com/check"

    payload = payload_start + words_string + payload_end

    with open('../resources/secure/rapidapi-key') as key_file:
        key = key_file.read()
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "jspell-checker.p.rapidapi.com",
        'x-rapidapi-key': key
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code != 200:
        print("Error: " + str(response.status_code) + ", " + response.text)
    else:
        handle_response(response.text, config, words)


def handle_suggestion(config, suggestions, suggestion):
    i = 0
    if len(suggestion) != 5:
        return
    for char in suggestion:
        if char not in config['alphabet']:
            return
        if char in config['invalid_letters']:
            return
        for valid_letter in config['valid_letters']:
            if char == valid_letter['letter']:
                if i in valid_letter['invalid_positions']:
                    return
            else:
                if i in valid_letter['valid_positions']:
                    return
        i = i + 1
    for valid_letter in config['valid_letters']:
        if valid_letter['letter'] not in suggestion:
            return
    suggestions.add(suggestion)


def handle_response(txt, config, words: list):
    spell_response = json.loads(txt)
    suggestions = set()
    for element in spell_response['elements']:
        for error in element['errors']:
            print('removing: ' + error['word'])
            words.remove(error['word'])
            for suggestion in error['suggestions']:
                handle_suggestion(config, suggestions, suggestion)
    for word in words:
        suggestions.add(word)
    for suggestion in suggestions:
        print('suggestion: ' + suggestion)


if __name__ == "__main__":
    find_word()
