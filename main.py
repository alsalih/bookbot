# Author:   Haidar Alsalih
# Date  :   14/01/2025
#
# Aim   :   create a bookbot terminal program which reads and analyses a 
#           plaintext book for useful indicators such as word, 
#           sentence, and paragraph counts and mean lengths, most and least 
#           frequent words, as well as alphabet frequencies.
#
# Notes :   Text Analyser assumes text files are plaintext files and filenames
#           use dashes (-) instead of spaces, e.g., "romeo-and-juliet.txt"

import os

def main():
    """Text Analyser analyses text for numerous indicators such as word, 
       sentence, and paragraph counts and mean lengths, most and least frequent 
       words, as well as alphabet frequencies."""
    # ************************************************************************ #
    # section 1: user chooses book for bookbot to analyse
    # ************************************************************************ #

    # list books

    # library is set to the directory/folder where books are stored
    library = 'books'
    books = []
    
    print("List of books: \n")
    # use os.listdir() method to find books in library folder and list them
    for book in os.listdir(library):
        books.append(book)
        book_title = " ".join(book[:-4].split("-")).title()
        print(book_title)

    # get path to user's desired book
    book_path = input("\nEnter name of book to analyse: ")
    book_path = "books/" + "-".join(book_path.split(" ")).lower() + ".txt"

    # ************************************************************************ #
    # section 2: bookbot analyses the book and displays the results in a report 
    # ************************************************************************ #

    text = get_book_text(book_path)

    words = get_words(text)
    num_words = len(words)
    # words_mean_length = get_mean_length(words)
    # num_unique_words = len(get_unique_words(words))

    # # to do if time permits
    # words_most_freq = None
    # words_least_freq = None
    # # END to do

    sentences = get_sentences(text)
    num_sentences = len(sentences)
    # sentences_mean_length = get_mean_length(sentences)

    paragraphs = get_paragraphs(text)
    num_paragraphs = len(paragraphs)
    # paragraphs_mean_length = get_mean_length(paragraphs)

# *** END main() *** 

def get_book_text(path):
    """given a file path to a book, returns the book's text"""
    with open(path) as book:
        return book.read()
    
def get_words(text):
    """given a text, returns a list of its words"""
    return text.split()

def get_mean_length(text, unit = "words"):
    """given a list of texts (in words, sentences, or paragraphs), and a unit
    of either characters or words, returns the mean length """

def get_sentences(text):
    """given a text, returns a list of its sentences"""

    foo = text.split()
    sentence_end = [".", "!", "?", "\""]

    sentences = []

    start = 0
    end = 0
    for i in range(0, len(foo)):
        if foo[i][len(foo[i]) - 1] in sentence_end:
            end = i
            sentence = ""
            for j in range(start, end):
                sentence += foo[j] + " "
            sentence += foo[end]
            sentences.append(sentence)
            start = end + 1

    return sentences

def get_paragraphs(text):
    """given a text, returns a list of its paragraphs"""
    return text.split("\n\n")















# def get_book_text(path):
#     """takes a path to a book as input, and returns the book's text"""
#     with open(path) as f: # opening the book file
#         return f.read() # returning the result of reading the file

# def get_num_words(text):
#     """takes a book's text as input, and returns the number of words in the 
#     text"""
#     words = text.split()
#     return len(words)

# def get_char_frequencies(text):
#     """takes a book's text as input, and returns the frequencies of each letter 
#     of the alphabet"""
#     char_freqs = dict()

#     for char in text:
#         if char.isalpha():
#             lowered = char.lower()
#             if lowered in char_freqs:
#                 char_freqs[lowered] += 1
#             else:
#                 char_freqs[lowered] = 1
    
#     return char_freqs

# def get_mean_word_length(text):
#     pass

# def sort_freqs(dict):
#     sorted_freqs = []
#     for freq in dict:
#         sorted_freqs.append({"char": freq, "frequency": dict[freq]})

#     def sort_on(dict):
#         return dict["frequency"]
        
#     sorted_freqs.sort(reverse=True, key=sort_on)

#     return sorted_freqs

# def get_text_report(book_path, num_words, char_freqs):
#     text_report = "\n**************************************************\n"
#     text_report += f"*** Begin Report of {book_path} ***\n"
#     text_report += "**************************************************\n\n"

#     text_report += f"There were {num_words} words found in {book_path}\n"
#     for char in char_freqs:
#         text_report += f"The '{char["char"]}' character was found \
#                         {char["frequency"]} times.\n"
    
#     text_report += "\n*** End Report ***"

#     return text_report

if __name__ == "__main__":
    main()