def is_pangram(sentence):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in abc:
        result = True if letter in sentence else False
    return result
