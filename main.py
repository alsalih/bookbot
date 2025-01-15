def main():
    """BookBot analyses a book's text for numerous indicators such as word count, alphabet frequency, and more"""
    book_path = "books/frankenstein.txt" # set path variable to where the book is

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    alphabet_frequencies = get_char_frequencies(text)

    print(f"{num_words} words found in the document")
    print(alphabet_frequencies)

def get_book_text(path):
    """takes a path to a book as input, and returns the book's text"""
    with open(path) as f: # opening the book file
        return f.read() # returning the result of reading the file

def get_num_words(text):
    """takes a book's text as input, and returns the number of words in the text"""
    words = text.split()
    return len(words)

def get_char_frequencies(text):
    """takes a book's text as input, and returns the frequencies of each letter of the alphabet"""
    char_freqs = dict()

    for char in text:
        lowered = char.lower()
        if lowered in char_freqs:
            char_freqs[lowered] += 1
        else:
            char_freqs[lowered] = 1
    
    return char_freqs

main()