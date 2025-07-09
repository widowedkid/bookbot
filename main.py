from stats import get_word_count, get_char_count, sort_char_values
import sys  

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
   # get_word_count(book_text)
    #print(sort_char_values(get_char_count(book_text)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    get_word_count(get_book_text(book_path))
    sort_char_values(get_char_count(get_book_text(book_path)))
    print("============= END ===============")


main()