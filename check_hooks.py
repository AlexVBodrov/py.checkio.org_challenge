"""
завести пустой стек

для каждого символа строки
  если он присутствует в наборе скобок
    если он отсутствует в словаре соответствий, т. е. это открывающая скобка
      добавить в стек этот символ
    иначе он закрывающая скобка
      если значение из словаря соответствий отличается от вершины стека
        return false
      иначе
        выкинуть последний элемент стека

return стек пуст
"""

a = 'a = (eqwe):[a,s,d]}'
b = '}{dasd())dasd[dasd]'
c = 'v = ((dqewqeqweqwe)'

def check(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else: return False
    return (not stack)

str1 = '[{([[[<>]]])(<>)(){}}]'
str2 = ']()(){<>}[[()]]'
str3 = '[(sjd),"2"],{2:3}, [<>]'
str4 = '{[[[[((()))]]<]>]}'

print(check(str1))  #True
print(check(str2))  #False
print(check(str3))  #True
print(check(str4))  #False

def balanced(s):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


print('-' * 35)
test_cases = ("{[()]}", "{[(])}", "}{[[(())]]}}")
for s in test_cases:
    print(s, balanced(s))


def is_matched(expression):
    """
    Finds out how balanced an expression is.
    With a string containing only brackets.

    >>> is_matched('[]()()(((([])))')
    False
    >>> is_matched('[](){{{[]}}}')
    True
    """
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in expression:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue



print('-' * 35)
test_cases = ("{[()]}", "{[(])}", "}{[[(())]]}}")
for s in test_cases:
    print(s, is_matched(s))