def evaluate(expression):
    def parse(tokens):
        token = tokens.pop(0)
        if token == '(':
            result = calculate(tokens)
            tokens.pop(0)  # pop the closing ')'
            return result
        else:
            return int(token)

    def calculate(tokens):
        total = parse(tokens)

        while tokens:
            token = tokens.pop(0)
            if token in '+-*/':
                next_value = parse(tokens)
                if token == '+':
                    total += next_value
                elif token == '-':
                    total -= next_value
                elif token == '*':
                    total *= next_value
                elif token == '/':
                    total /= next_value
            else:
                break

        return total

    tokens = expression.replace(' ', '').replace('(', ' ( ').replace(')', ' ) ').split()
    return calculate(tokens)

expression = input("请输入运算式: ")
result = evaluate(expression)
print("结果:", result)
