import re
import sys

input = input('Digite o CPF: ')

user_cpf = re.sub(
    r'[^0-9]',
    '',
    input
)

sequencial_input = input == input[0] * len(input)

if sequencial_input:
    print('Você enviou dados sequenciais')
    sys.exit()

nine_digits = user_cpf[:9]

multiplyed_by = 10

result = 0
for digit in nine_digits:
    result += int(digit) * multiplyed_by
    multiplyed_by -= 1

digit1 = (result * 10) % 11

digit1 = digit1 if digit1 <= 9 else 0

ten_digits = nine_digits + str(digit1)
multiplyed_by_2 = 11

result2 = 0
for digit in ten_digits:
    result2 += int(digit) * multiplyed_by_2
    multiplyed_by_2 -= 1
digit2 = (result2 * 10) % 11
digit2 = digit2 if digit2 <= 9 else 0


calculate_cpf = f'{nine_digits}{digit1}{digit2}'

if user_cpf == calculate_cpf:
    print(f'{user_cpf} é válido')
else:
    print('CPF inválido')