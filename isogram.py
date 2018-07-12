def is_isogram(string):
    unique_letter_set = set()
    hiffen_qtd = 0
    string = string.replace(" ", "")
    string = string.lower()
    for letter in string:
        if letter == '-':
            hiffen_qtd += 1     
        else:
            unique_letter_set.add(letter)
    return len(string) == len(unique_letter_set) + hiffen_qtd