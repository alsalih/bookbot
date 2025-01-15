# Author: Haidar Alsalih
# Date  : 14/01/2025
# Aim   : create a bookbot terminal program which reads and analyses a plaintext
#         book for useful indicators such as word count, alphabet frequencies,
#         number of unique words, and more
# Notes : bookbot assumes books are in the 'books' directory and that book names
#         are .txt files split by dashes(*). For example: 'romeo-and-juliet.txt'

# import os to list books for user to choose from
import os

def main():
    """BookBot analyses a book's text for numerous indicators such as word 
       count, alphabet frequency, and more"""
    # *** User chooses book for bookbot to analyse ***

    # * list books *

    library = 'books'
    books = []
    # use os.listdir() method to find books in library folder
    for book in os.listdir(library):
        books.append(book)
        book_title = " ".join(book[:-4].split("-")).title()
        print(book_title)

    # * get path to user's desired book *
    book_path = input("Enter name of book to analyse: ")
    book_path = "books/" + "-".join(book_path.split(" ")).lower() + ".txt"

    # *** bookbot analyses book and displays results in a report ***
    
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
    text_report = "\n**************************************************\n"
    text_report += f"*** Begin Report of {book_path} ***\n"
    text_report += "**************************************************\n\n"

    text_report += f"There were {num_words} words found in {book_path}\n"
    for char in char_freqs:
        text_report += f"The '{char["char"]}' character was found {char["frequency"]} times.\n"
    
    text_report += "\n*** End Report ***"

    return text_report
    
main()