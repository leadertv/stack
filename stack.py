class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(input_string):
    stack = Stack()
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for char in input_string:
        if char in bracket_pairs:  # открывающая скобка
            stack.push(char)
        elif char in bracket_pairs.values():  # закрывающая скобка
            if stack.is_empty():
                return "Несбалансированно"
            top_char = stack.pop()
            if bracket_pairs.get(top_char) != char:  # проверяем соответствие
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


# Тестируем.
print(is_balanced("(((([{}]))))"))  # Сбалансированно
print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(is_balanced("{{[()]}}"))  # Сбалансированно
print(is_balanced("}{"))  # Несбалансированно
print(is_balanced("{{[(])]}}"))  # Несбалансированно
print(is_balanced("[[{())}]"))  # Несбалансированно
