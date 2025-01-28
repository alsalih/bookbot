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
    # Section 1: user chooses text for analyser to analyse
    # ************************************************************************#

    # Library is set to the directory/folder where texts are stored
    library = 'texts'
    list_texts(library)

    # Loop to get path to user's desired text
    while True:
        text_title = input("\nEnter name of text to analyse: ")
        text_path = f"{library}/" + "-".join(text_title.split(" ")).lower() + ".txt"
        if os.path.isfile(text_path):
            break
        else:
            print(f"Error: The file {text_path} was not found. Please try again.")

    # ************************************************************************#
    # Section 2: analyser analyses the text and displays the results in a report
    # ************************************************************************#

    text_matter = get_text_matter(text_path)
    report_dict = {}

    # Basic statistics

    words = get_words(text_matter)
    report_dict["num_words"] = len(words)
    report_dict["words_mean_length"] = round(mean_len(words, "characters"), 2)

    sentences = get_sentences(text_matter)
    report_dict["num_sentences"] = len(sentences)
    report_dict["sent_mean_len"] = round(mean_len(sentences, "words"), 2)

    paragraphs = get_paragraphs(text_matter)
    report_dict["num_paragraphs"] = len(paragraphs)
    report_dict["parags_mean_len"] = round(mean_len(paragraphs, "words"), 2)

    # Word frequencies

    report_dict["word_frequencies"] = word_frequencies(words)

    text_report = get_text_report(text_title, report_dict)

    print(text_report)

# *** END main() *** 

def list_texts(library):
    """Lists the texts available in the library folder."""

    # use os.listdir() method to find texts in library folder and list them
    print("\nAvailable texts: \n")
    for text in os.listdir(library):
        print(" ".join(text[:-4].split("-")).title())

def get_text_matter(path):
    """given a file path to a text-file, returns the file's text matter."""
    try:
        with open(path, 'r') as text:
            return text.read()
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        return ""
    except IOError:
        print(f"Error: An error occurred while reading the file {path}.")
        return ""
    
def get_words(text_matter):
    """given a text's matter, returns a list of its words."""
    return text_matter.split()

def mean_len(text_matter, unit):
    """given text matter as a list (words, sentences, or paragraphs), and a unit
    of either characters or words, returns the mean length in that unit."""
    mean_len = 0

    if unit == "characters":
        return sum(len(word) for word in text_matter) / len(text_matter)
    elif unit == "words":
        return sum(len(piece.split()) for piece in text_matter) / len(text_matter)
    else:
        raise Exception("Error: Invalid unit. Please enter 'characters' or 'words'.")

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

def word_frequencies(words):
    freq_dict = {}
    for word in words:
        if len(word) == 1:
            cp_word = word.strip(".,!?\"")
        else:
            cp_word = word.strip(".,!?\"").lower()

        if cp_word in freq_dict:
            freq_dict[cp_word] += 1
        else:
            freq_dict[cp_word] = 1
        
    return list(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))

def get_most_frequent_words(word_frequencies):
    """given a list of word frequencies, returns the 10 most frequent words."""
    return word_frequencies[:10]

def get_least_frequent_words(word_frequencies):
    """given a list of word frequencies, returns the 10 least frequent words,
        with the word occuring at least 0.2% of the time."""
    
    least_freq_words = []
    for word in word_frequencies:
        if word[1] > len(word_frequencies) / 500:
            least_freq_words.append(word)
    return least_freq_words[-11:-1]

def get_text_report(text_title, report_dict):
    """
    Generates a formatted text report based on the analysis of the text.

    Parameters:
    text_title (str): The title of the text being analyzed.
    report_dict (dict): A dictionary containing the analysis results.

    Returns:
    a formatted string containing the text report.
    """
    
    # various statistics
    num_words = report_dict["num_words"]
    words_mean_length = report_dict["words_mean_length"]
    num_sentences = report_dict["num_sentences"]
    sent_mean_len = report_dict["sent_mean_len"]
    num_paragraphs = report_dict["num_paragraphs"]
    parags_mean_len = report_dict["parags_mean_len"]

    # 10 most and 10 least frequent words
    most_frequent_words_lst = get_most_frequent_words(report_dict["word_frequencies"])
    least_frequent_words_lst = get_least_frequent_words(report_dict["word_frequencies"])

    stats = lambda x, y: f"|{x:^25}|{y:^25}|\n"

    cell_border = "-" * 53 + "\n"

    # Greeting
    text_report = "\n...\n\nThank you for using Text Analyser!\n\n"
    text_report += f"Here is your report on {text_title.title()}:\n\n"

    # Basic stats
    text_report += cell_border
    text_report += "|{:^25}|{:^25}|\n".format("Num. Words", "Mean Word length")
    text_report += cell_border
    text_report += stats(num_words, words_mean_length)
    text_report += cell_border + "\n"

    text_report += cell_border
    text_report += "|{:^25}|{:^25}|\n".format("Num. Sentences", "Mean Sent. length")
    text_report += cell_border
    text_report += stats(num_sentences, sent_mean_len)
    text_report += cell_border + "\n"

    text_report += cell_border
    text_report += "|{:^25}|{:^25}|\n".format("Num. Paragraphs", "Mean Para. length")
    text_report += cell_border
    text_report += stats(num_paragraphs, parags_mean_len)
    text_report += cell_border

    # Word frequencies
    text_report += "\nMost Frequent Words:\n"
    text_report += "\n {:<15}: {:^8}\n".format("Word", "Frequency")
    text_report += cell_border
    for word in most_frequent_words_lst:
        text_report += f"{word[0]:<15}:{word[1]:^8}\n"
    text_report += cell_border
    
    text_report += "\nLeast Frequent Words (>0.2% to keep stat meaningful):\n"
    text_report += "\n {:<15}: {:^8}\n".format("Word", "Frequency")
    text_report += cell_border
    for word in least_frequent_words_lst:
        text_report += f"{word[0]:<15}:{word[1]:^8}\n"
    text_report += cell_border
    
    return text_report

if __name__ == "__main__":
    main()