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

# --------------------------------------------------------------------------------------------------------------------- #

class Parser:
    def __init__(self, expression):
        self.tokens = expression.replace(' ', '').replace('(', ' ( ').replace(')', ' ) ').split()
        self.current_token_index = 0

    def parse(self):
        return self.expr()

    def expr(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            operator = self.current_token()
            self.next_token()
            if operator == '+':
                result += self.term()
            elif operator == '-':
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.current_token() in ('*', '/'):
            operator = self.current_token()
            self.next_token()
            if operator == '*':
                result *= self.factor()
            elif operator == '/':
                result /= self.factor()
        return result

    def factor(self):
        token = self.current_token()
        if token.isdigit():  # If the token is a number
            self.next_token()
            return int(token)
        elif token == '(':
            self.next_token()
            result = self.expr()
            self.next_token()  # Skip the closing ')'
            return result

    def current_token(self):
        return self.tokens[self.current_token_index] if self.current_token_index < len(self.tokens) else None

    def next_token(self):
        self.current_token_index += 1


# 使用示例
expression = input("请输入运算式: ")
parser = Parser(expression)
result = parser.parse()
print("结果:", result)

# ---------------------------------------------------------------------------------------------------------------------
class Parser:
    def __init__(self, expression):
        self.tokens = expression.replace(' ', '').replace('(', ' ( ').replace(')', ' ) ').split()
        self.current_token_index = 0

    def parse(self):
        return self.expr()

    def expr(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            operator = self.current_token()
            self.next_token()
            if operator == '+':
                result += self.term()
            elif operator == '-':
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.current_token() in ('*', '/', '%'):
            operator = self.current_token()
            self.next_token()
            if operator == '*':
                result *= self.factor()
            elif operator == '/':
                result /= self.factor()
            elif operator == '%':
                result %= self.factor()
        return result

    def factor(self):
        result = self.base()
        while self.current_token() == '**':
            self.next_token()
            result **= self.base()  # 处理次方运算
        return result

    def base(self):
        token = self.current_token()
        if token.isdigit():  # 如果令牌是数字
            self.next_token()
            return int(token)
        elif token == '(':
            self.next_token()
            result = self.expr()
            self.next_token()  # 跳过闭合的 ')'
            return result

    def current_token(self):
        return self.tokens[self.current_token_index] if self.current_token_index < len(self.tokens) else None

    def next_token(self):
        self.current_token_index += 1


# 使用示例
expression = input("请输入运算式: ")
parser = Parser(expression)
result = parser.parse()
print("结果:", result)
