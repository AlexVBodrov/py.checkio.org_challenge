"""
В заданной строке вы должны перевернуть каждое слово, но слова должны оставаться на своих местах.
Input: A string.
Output: A string.
Example:
backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'
Предварительное условие: строка состоит только из буквенных символов и пробелов.
"""
def backward_string_by_word(text: str) -> str:
    # your code here
    if len(text)>1:
        myList = text.split(' ')
        c = []
        for i in myList:
            c.append(''.join(reversed(i)))
        c = ' '.join(c)
        print(c)
    else:
        return text
    return c
    #return ' '.join(word[::-1] for word in text.split(' '))
"""
def backward_string_by_word(text: str) -> str:

    split_text = text.split(' ')                        # Split the string into a list
    reversed_text = ' '.join(reversed(split_text))      # Reverse the order (so "hello  world" becomes "world  hello" and join the list to make a string again

    return reversed_text[::-1]                          # negative slicing returns everything backwards which gives us "olleh  dlrow"
"""

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")