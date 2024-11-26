import os


def convert_words_to_lower(words: str) -> str:
    return words.lower()


def remove_special_chars(word: str) -> str:
    return "".join([w for w in word if w.isalnum()])


def process_words(line: str) -> str:
    word_to_lower = convert_words_to_lower(line)
    return remove_special_chars(word_to_lower)


def create_list_of_words(file: str) -> list[str]:
    words: list = []
    with open(file, 'r') as opened_file:
        line = opened_file.read()
        words.append(process_words(line))
    return words


def word_count(file: str) -> dict[str, int]:
    words = create_list_of_words(file)
    number_of_words: dict = {}
    words_string = "".join(w for w in words)
    for word in words:
        if word not in number_of_words:
            number_of_words[word] = words_string.count(word)
    return number_of_words




test_file = os.getcwd() + "/test.txt"
word_count(test_file)
