import sys
from stats import word_count, char_count, sort_char

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)

    num_words = word_count(book_text)
    char_counts = char_count(book_text)
    sorted_characters = sort_char(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_characters:
        print(f"{entry['character']}: {entry['count']}")

    print("============= END ===============")

main()





