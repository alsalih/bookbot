# Author:   Haidar Alsalih
# Date  :   14/01/2025
#
# Aim   :   Create a text analyser terminal program which reads and analyses a 
#           text file for useful indicators such as word, sentence, and
#           paragraph counts, and mean lengths; most and least frequent words,
#           and alphabet frequencies.
#
# Notes :   Text Analyser assumes text files are plaintext files and filenames
#           use dashes (-) instead of spaces, e.g., "romeo-and-juliet.txt"

import os

def main():
    """Text Analyser analyses text for numerous indicators such as word, 
       sentence, and paragraph counts and mean lengths, most and least frequent 
       words, as well as alphabet frequencies."""
    # ************************************************************************ #
    # section 1: user chooses text for analyser to analyse
    # ************************************************************************ #

    # library is set to the directory/folder where texts are stored
    library = 'texts'
    list_texts(library)

    # get path to user's desired text
    text = input("\nEnter name of text to analyse: ")
    text_path = f"{library}/" + "-".join(text.split(" ")).lower() + ".txt"

    # ************************************************************************ #
    # section 2: analyser analyses the text and displays the results in a report 
    # ************************************************************************ #

    text = get_text(text_path)

    words = get_words(text)
    num_words = len(words)
    words_mean_length = round(get_mean_length(words, "characters"), 2)
    # num_unique_words = len(get_unique_words(words))

    # # to do if time permits
    # words_most_freq = None
    # words_least_freq = None
    # # END to do

    sentences = get_sentences(text)
    num_sentences = len(sentences)
    sentences_mean_length = round(get_mean_length(sentences, "words"), 2)

    paragraphs = get_paragraphs(text)
    num_paragraphs = len(paragraphs)
    paragraphs_mean_length = round(get_mean_length(paragraphs, "words"), 2)

    print(f"Num. Words: {num_words}\nmean word length: {words_mean_length} characters\n\
num. sentences: {num_sentences}\nmean sent. length: {sentences_mean_length} words\n\
num. paragraphs: {num_paragraphs}\nmean para. length: {paragraphs_mean_length} words")

# *** END main() *** 

def list_texts(library):
    texts = []
    
    print("List of texts: \n")
    # use os.listdir() method to find texts in library folder and list them
    for text in os.listdir(library):
        texts.append(text)
        text_title = " ".join(text[:-4].split("-")).title()
        print(text_title)

def get_text(path):
    """given a file path to a text-file, returns the file's text contents."""
    with open(path) as text:
        return text.read()
    
def get_words(text):
    """given a text, returns a list of its words."""
    return text.split()

def get_mean_length(text, unit):
    """given a text as a list (words, sentences, or paragraphs), and a unit
    of either characters or words, returns the mean length in that unit."""
    mean_length = 0

    if unit == "characters":
        for word in text:
            mean_length += len(word)
        mean_length = mean_length / len(text)

    if unit == "words":
        for piece in text:
            mean_length += len(piece.split())
        mean_length = mean_length / len(text)

    return mean_length

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
    """given a text, returns a list of its paragraphs."""
    return text.split("\n\n")













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