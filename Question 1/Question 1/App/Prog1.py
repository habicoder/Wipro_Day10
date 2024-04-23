def find_short_long_word(words_list):
    shortest_word = words_list[0]
    longest_word = words_list[0]
    for word in words_list:
        if len(word) < len(shortest_word):
            shortest_word = word
        elif len(word) >= len(longest_word):
            longest_word = word
    return (shortest_word, longest_word)
