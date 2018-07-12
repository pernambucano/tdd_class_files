def word_count(phrase):
    
    list_of_words = phrase.split(" ")

    result_dict = {}
    for word in list_of_words:
        if word in result_dict.keys():
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict