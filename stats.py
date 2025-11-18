import sys

character_dic = {}

new_dics = []

def word_count(book_string):
    num_words = 0
    for word in book_string.split():
        num_words += 1
    return num_words

def character_count(book_string):
    lower_case_book_string = book_string.lower()
    for ch in lower_case_book_string:
        if ch not in character_dic:
            character_dic[ch] = 1
        else:
            character_dic[ch] += 1
    return character_dic

def dic_sort(character_dic):
    def sort_on(small_dic):
        return small_dic["num"]

    for key, value in character_dic.items():
        small_dic = {}
        small_dic["char"] = key
        small_dic["num"] = value
        new_dics.append(small_dic)
    
    new_dics.sort(reverse=True, key=sort_on)
    return new_dics