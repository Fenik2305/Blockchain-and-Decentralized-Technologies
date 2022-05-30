def hexToLittleEndian(s):
    pointer = len(s) - 1
    while s[pointer] == '0':
        pointer -= 1
    return int(s[:pointer + 1] if pointer % 2 == 1 else s[:pointer + 2], 16)

def hexToBigEndian(s):
    return int(s, 16)

def littleEndianToHex(s):
    print(s)
    return '0x' + hex(int(s))[2:].upper()

def bigEndianToHex(s):
    print(s)
    return '0x' + hex(int(s))[2:].upper()

value = input() #0x{hex}
print('Number of bytes:', len(value[2:]) // 2)
print('Little-endian:', hexToLittleEndian(value))
print('Big-endian:', hexToBigEndian(value))
#Конвертування з ендіанів у 16-річну систему здійснюється за допомогою функцій littleEndianToHex і bigEndianToHex