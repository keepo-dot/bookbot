from stats import get_num_words, count_letters, sort_dictionary
import sys


def get_book_text(book_path):
    with open(book_path) as f:
            return f.read()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    


    book_path = f"{sys.argv[1]}"

    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    
    letters_dict = count_letters(text)
    
    sorted_dict = sort_dictionary(letters_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_item in sorted_dict:
        char = char_item["char"]
        count = char_item["count"]
        if char.isalpha():
            print(f"{char}: {count}")



    print("============= END ===============")
    



main()