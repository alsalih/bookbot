# Author        :   Haidar Alsalih
# Date          :   14/01/2025
#
# Aim           :   Create a text analyser terminal program which reads and 
#                   analyses a text file for useful indicators such as word, 
#                   sentence, and paragraph counts, and mean lengths; most and 
#                   least frequent words, and alphabet frequencies.
#
# Definitions   :   Text: the text itself i.e. a book, magazine, novel, etc.
#                   Text Matter: the content of that text (e.g. the words
#                       in a book)
#
# Notes :           Text Analyser assumes text files are plaintext files and 
#                   filenames use dashes (-) instead of spaces, e.g., 
#                   "romeo-and-juliet.txt"

import os

def main():
    """Text Analyser analyses text for numerous indicators such as word, 
       sentence, and paragraph counts and mean lengths, most and least frequent 
       words, as well as alphabet frequencies."""
    # ************************************************************************#
    # section 1: user chooses text for analyser to analyse
    # ************************************************************************#

    # library is set to the directory/folder where texts are stored
    library = 'texts'
    list_texts(library)

    # get path to user's desired text
    text_title = input("\nEnter name of text to analyse: ")
    text_path = f"{library}/" + "-".join(text_title.split(" ")).lower() + ".txt"

    # ************************************************************************#
    # section 2: analyser analyses the text and displays the results in a report 
    # ************************************************************************#

    text_matter = get_text_matter(text_path)

    words = get_words(text_matter)
    num_words = len(words)
    words_mean_length = round(get_mean_length(words, "characters"), 2)

    sentences = get_sentences(text_matter)
    num_sentences = len(sentences)
    sentences_mean_length = round(get_mean_length(sentences, "words"), 2)

    paragraphs = get_paragraphs(text_matter)
    num_paragraphs = len(paragraphs)
    paragraphs_mean_length = round(get_mean_length(paragraphs, "words"), 2)

    print(get_text_report(text_title, num_words, words_mean_length, sentences, 
        num_sentences, sentences_mean_length, paragraphs, num_paragraphs, 
        paragraphs_mean_length))

# *** END main() *** 

def list_texts(library):
    texts = []
    
    print("List of texts: \n")
    # use os.listdir() method to find texts in library folder and list them
    for text in os.listdir(library):
        texts.append(text)
        text_title = " ".join(text[:-4].split("-")).title()
        print(text_title)

def get_text_matter(path):
    """given a file path to a text-file, returns the file's text matter."""
    with open(path) as text:
        return text.read()
    
def get_words(text_matter):
    """given a text's matter, returns a list of its words."""
    return text_matter.split()

def get_mean_length(text_matter, unit):
    """given text matter as a list (words, sentences, or paragraphs), and a unit
    of either characters or words, returns the mean length in that unit."""
    mean_length = 0

    if unit == "characters":
        for word in text_matter:
            mean_length += len(word)
        mean_length = mean_length / len(text_matter)

    if unit == "words":
        for piece in text_matter:
            mean_length += len(piece.split())
        mean_length = mean_length / len(text_matter)

    return mean_length

def get_sentences(text_matter):
    """given a text's matter, returns a list of its sentences"""

    words = text_matter.split()
    sentence_end = [".", "!", "?", "\""]

    sentences = []

    start = 0
    end = 0
    for i in range(0, len(words)):
        if words[i][len(words[i]) - 1] in sentence_end:
            end = i
            sentence = ""
            for j in range(start, end):
                sentence += words[j] + " "
            sentence += words[end]
            sentences.append(sentence)
            start = end + 1

    return sentences

def get_paragraphs(text_matter):
    """given a text's matter, returns a list of its paragraphs."""
    return text_matter.split("\n\n")

def get_text_report(text_title, num_words, words_mean_length, sentences, 
    num_sentences, sentences_mean_length, paragraphs, num_paragraphs, 
    paragraphs_mean_length):
    
    def space(n, content):
        result = ""
        x = int((n - len(str(content))) / 2)

        for i in range(0, x):
            result += " "

        result += str(content)

        for i in range(0, x):
            result += " "

        return result

    text_report = "\n...\n"
    text_report += "\nThank you for using Text Analyser!\n\n"
    text_report += f"Here is your text report on {text_title.title()}:\n\n"
    text_report += "---------------------------------------------------\n"
    text_report += "|      Num. Words      |      Mean Word length    |\n"
    text_report += "---------------------------------------------------\n"
    text_report += f"|{space(22, num_words)}|{space(26, words_mean_length)}|\n"
    text_report += "---------------------------------------------------\n"
    
    return text_report

if __name__ == "__main__":
    main()