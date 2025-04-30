def word_count(file_contents):
    words = file_contents.split()   
    count = len(words)
    return count

def character_count(file_contents):
    count = {}
    low_characters = file_contents.lower()
    for item in low_characters:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

def chars_to_sorted_list(char_count_dict):
    char_list = []

    for char, num in char_count_dict.items():
        char_dict = {"char": char, "num": num}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort)   

    return char_list 

def sort(dict):
    return dict["num"]

            
            

    