def calculator(expression):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Должно содержать хотя бы один знак {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return{
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
                # if sign == '+':
                #     return left + right
                # elif sign == '-':
                #     return left - right
                # elif sign == '*':
                #     return left * right
                # elif sign == '/':
                #     return left / right
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calculator('8/2'))
