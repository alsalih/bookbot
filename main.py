def main():
    """BookBot analyses a book's text for numerous indicators such as word count, alphabet frequency, and more"""
    book_path = "books/frankenstein.txt" # set path variable to where the book is

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_frequencies = sort_freqs(get_char_frequencies(text))

    print(get_text_report(book_path, num_words, character_frequencies))

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
        if char.isalpha():
            lowered = char.lower()
            if lowered in char_freqs:
                char_freqs[lowered] += 1
            else:
                char_freqs[lowered] = 1
    
    return char_freqs



def sort_freqs(dict):
    sorted_freqs = []
    for freq in dict:
        sorted_freqs.append({"char": freq, "frequency": dict[freq]})

    def sort_on(dict):
        return dict["frequency"]
        
    sorted_freqs.sort(reverse=True, key=sort_on)

    return sorted_freqs



def get_text_report(book_path, num_words, char_freqs):
    text_report = "**************************************************" + "\n"
    text_report += f"*** Begin Report of {book_path} ***" + "\n"
    text_report += "**************************************************" + "\n\n"

    text_report += f"There were {num_words} words found in {book_path}" + "\n"
    for char in char_freqs:
        text_report += f"The '{char["char"]}' character was found {char["frequency"]} times." + "\n"
    
    text_report += "\n*** End Report ***"

    return text_report
    
main()