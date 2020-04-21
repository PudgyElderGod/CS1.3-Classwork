import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    left = 0
    #incase the text is empty
    if len(text)>0:
        right = len(text)-1
    else: 
        right = len(text)
    #while the center letter hasnt been reacher
    while left < right:
        #checks to see if the current elements are letters, if not then skip that element
        while text[left] not in string.ascii_letters:
            left+=1
        while text[right] not in string.ascii_letters:
            right-=1
        print(left)
        print(right)
        #if they dont match then it isnt a palindrome
        temp1 = text[right].lower()
        temp2 = text[left].lower()
        if temp1 != temp2:
            return False
        left+=1
        right-=1
    return True

def is_palindrome_recursive(text, left=None, right=None):
    #first time running the function
    if right == None and left == None:
        left = 0
        if len(text)>0:
            right = len(text)-1
        else: 
            right = len(text)
    if left < right:
        #check to see if the current elements are letters, if not skip them
        while text[left] not in string.ascii_letters:
            left+=1
        while text[right] not in string.ascii_letters:
            right-=1
        #if they dont match then it isnt a palindrome
        temp1 = text[right].lower()
        temp2 = text[left].lower()
        if temp1 != temp2:
            return False
        left+=1
        right-=1
        return is_palindrome_recursive(text, left, right)
    return True

def standardize(text):
    neo = ""
    for t in text:
        if t in string.ascii_letters:
            neo += t.lower()
    return neo


def main():
    import sys
    args = sys.argv[1:] 
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


assert is_palindrome("Go hang a salami, I'm a lasagna hog.") is True


