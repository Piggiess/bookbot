import sys
from stats import word_count
from stats import character_count
from stats import dic_sort

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
book_string = None
with open(book) as f:
    book_string = f.read()
character_dic = character_count(book_string)
new_dics = dic_sort(character_dic)

total_char_count = character_count(book_string)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}")
print("----------- Word Count ----------")
print(f"Found {word_count(book_string)} total words")
print("--------- Character Count -------")
for item in new_dics:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
    else:
        pass
print("============= END ===============")