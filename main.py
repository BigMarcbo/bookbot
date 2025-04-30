from stats import word_count
from stats import character_count
from stats import chars_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    char_counts = character_count(book_text)
    sorted_chars = chars_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()