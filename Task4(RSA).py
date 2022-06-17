def GCD(a, b):
    if b == 0:
        x = 1
        y = 0
        return x, y
    else:
        x1, y1 = GCD(b, a % b)
        x = y1
        y = x1 - int(a / b) * y1
        return x, y

p, q, e = 25013, 25031, 1000003
n, m = p * q, (p - 1) * (q - 1)

x, y = GCD(e, m)
d = (x + m) % m

publicKey = [e, n]
privateKey = [d, n]
print('Public Key:', publicKey, 'Private Key:', privateKey, sep='\n', end='\n')

def encode(message, publKey):
    e, n = publKey
    return [pow(ord(char), e, n) for char in message]

def decode(code, privKey):
    d, n = privKey
    return ''.join([chr(pow(el, d, n)) for el in code])

message = input('Enter the message to encrypt: ')
code = encode(message, publicKey)
print('Coded message:', code)
print('Decoded message:', decode(code, privateKey))