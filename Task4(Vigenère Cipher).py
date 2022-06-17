#созаём две матрицы-таблицы для шифровки и дешифровки
encrypt = [[chr(j + i if j + i < 123 else j + i - 26) for j in range(97, 123)] for i in range(0, 26)]
decrypt = [[chr(j - i if j - i >= 97 else j - i + 26) for j in range(97, 123)] for i in range(0, 26)]

def encode(message, key, p=0):
    result = ''
    for char in message:
        if 97 <= ord(char) <= 122: #если шифруемый символ - строчная латинска буква, то шифруем
            result += encrypt[ord(char) - 97][ord(key[p]) - 97]
            p = (p + 1) % len(key) #p - индекс символа ключа с которого начинаем (по умолчанию с первого)
        else:
            result += char #иначе просто добавляем символ к результирующей строке
    return result


def decode(code, key, p=0):
    result = ''
    for char in code:
        if 97 <= ord(char) <= 122 and 97 <= ord(key[p]) <= 122:
            result += decrypt[ord(key[p]) - 97][ord(char) - 97]
            p = (p + 1) % len(key)
        else:
            result += char
    return result

key = input('Enter the key to encrypt the message:\n')
message = input('Enter the message to encrypt:\n')
code = encode(message, key)
print(f'Encrypted message: \n{code}')
message = decode(code, key)
print(f'Decrypted code: \n{message}')
