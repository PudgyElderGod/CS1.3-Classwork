import string

values = "0123456789abcdefghijklmnopqrstuvwxyz"

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    temp = str(digits)
    temp = digits[::-1]
    dec = 0
    for x in range(len(temp)):
        power = base**x
        for y in range(len(values)-1):
            if temp[x] == values[y]:
                dec += y*power
    return dec

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)

    baseVer = ""
    while number!=0:
        remaind = number%base
        print(remaind)
        for a in range(36):
            if remaind == a:
                baseVer+=values[a]
                print(values[a])
                break
        number = int(number/base) 
        print(number)
    print(baseVer[::-1])
    return baseVer[::-1]



def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
   
    dec = decode(digits, base1)
    return encode(dec, base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    #main()
    encode(248975, 25)