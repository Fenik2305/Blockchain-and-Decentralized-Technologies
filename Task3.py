def numSplit(num):
    arr = []
    while num:
        arr.append((num & 2 ** 32 - 1))
        num = num >> 32
    return arr

def toLeft(num, shift):
    size = 32
    return ((num >> size - shift) | (num << shift)) & 2 ** 512 - 1

def chunkIter(text):
    while text:
        chunk = text & 2 ** 448 - 1
        size = len(bin(chunk)) - 2
        chunk = (chunk << 1) + 1
        chunk = chunk << (512 - size - 1)
        chunk += size
        yield chunk
        text = text >> 448

def SHA1(text, h0=0x67452301, h1=0xEFCDAB89, h2=0x98BADCFE, h3=0x10325476, h4=0xC3D2E1F0):
    hash = 0
    for chunk in chunkIter(text):
        w = numSplit(chunk)
        for i in range(16, 80):
            w.append(toLeft((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 5))
        A = h0
        B = h1
        C = h2
        D = h3
        E = h4
        for i in range(80):
            if 0 <= i <= 19:
                F = (B and C) or ((not B) and D)
                K = 0x5A827999
            elif 20 <= i <= 39:
                F = B ^ C ^ D
                K = 0x6ED9EBA1
            elif 40 <= i <= 59:
                F = (B and C) or (B and D) or (C and D)
                K = 0x8F1BBCDC
            elif 60 <= i <= 79:
                F = B ^ C ^ D
                K = 0xCA62C1D6
            temp = (toLeft(A, 5) + F + E + K + w[i]) % (2 ** 32)
            E = D
            D = C
            C = toLeft(B, 30)
            B = A
            A = temp
        h0 += A % (2 ** 32)
        h1 += B % (2 ** 32)
        h2 += C % (2 ** 32)
        h3 += D % (2 ** 32)
        h4 += E % (2 ** 32)
        s = h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4
        hash += s
        hash %= 1 << 512
    return hash

print('Enter the message you want to hash: ')
print('Result:', hex(SHA1(int.from_bytes(input().encode('UTF-8', 'surrogatepass'), 'big'))), sep='\n')
