#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

values = "0123456789abcdefghijklmnopqrstuvwxyz"

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    #reverses the number to decode
    temp = str(digits)
    temp = digits[::-1]
    #our decoded number
    dec = 0
    #loop through the reversed number string 
    for x in range(len(temp)):
        power = base**x
        #loop through the values string to find the value that matches the one in the reversed number string
        for y in range(len(values)-1):
            #check if the base number matches the conversion number
            if temp[x] == values[y]:
                dec += y*power
    return dec

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    baseVer = ""    #empty string to hold converted number
    #divide the number by the base number until its 0
    while number!=0:
        #the remainder of each division becomes part of the converted number
        remaind = number%base
        print(remaind)
        #finds the corresponding base number for the remainder
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
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
   
    dec = decode(digits, base1)
    return encode(dec, base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    #main()
    encode(248975, 25)