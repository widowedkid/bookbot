def get_word_count(text):
    count = 0
    for i in text.split():
        count += 1
    word_count = f"Found {count} total words"
    print("----------- Word Count ----------")
    print(word_count)


def sort_on(items):
    return items["num"]


def get_char_count(text):
    print("--------- Character Count -------")
    char_count = {}
    lowered = text.lower()
    for word in lowered.split():
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
    
def sort_char_values(char_values):
    sorte = char_values.items()
    f_list = []
    for char, num in sorte:
        l_list = {}
        l_list["char"] = char
        l_list["num"] = num
        f_list.append(l_list)
    f_list.sort(reverse=True, key=sort_on)
    for i in f_list:
        character = i['char']
        if character.isalpha():
            print(f"{i['char']}: {i['num']}")
    

               

