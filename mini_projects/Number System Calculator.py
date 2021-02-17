def dec_to_bin(num_dec):
    num_bin = ''
    while num_dec > 0:
        dig = num_dec % 2
        num_bin += str(dig)
        num_dec //= 2
    return num_bin[::-1]

def dec_to_oct(num_dec):
    num_oct = ''
    while num_dec > 0:
        dig = num_dec % 8
        num_oct += str(dig)
        num_dec //= 8
    return num_oct[::-1]

def dec_to_hex(num_dec):
    num_hex = ''
    while num_dec > 0:
        dig = num_dec % 16
        if dig > 9:
            dig = chr(64 + (dig - 9))
        num_hex += str(dig)
        num_dec //= 16
    return num_hex[::-1]

num_dec = int(input())
print(dec_to_bin(num_dec))
print(dec_to_oct(num_dec))
print(dec_to_hex(num_dec))