def get_num_words(text):
    words = text.split()
    return len(words)



def count_letters(text):
    letters_dict = {} # make dict
    for letters in text:
        lowercase_letters = letters.lower()
        if lowercase_letters in letters_dict:
            letters_dict[lowercase_letters] += 1
        else:
            letters_dict[lowercase_letters] = 1
    return letters_dict



def sort_dictionary(letters_dict):
    dict_list = []


    
    for char, count in letters_dict.items():
        unsorted_dict = {"char": char, "count": count}
        dict_list.append(unsorted_dict)
    
    
    
    def sort_value(dict_item):
        return dict_item["count"]
    


    dict_list.sort(reverse=True, key=sort_value)
    
    
    
    return dict_list
    
    

