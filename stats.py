def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha(): 
            sorted_list.append({
                "character": char,
                "count": count
            })

    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list
