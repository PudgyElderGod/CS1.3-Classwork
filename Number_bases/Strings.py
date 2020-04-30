def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    num = 0     #index to keep track of which letter in pattern you're comparing to you
    if len(pattern) == 0:
        return True 
    for letter in text:
        #if they arent equal and you're part of the way into comapring to the pattern
        if num>0 and letter != pattern[num]:
            num = 0
        # check if your current letter matches a letter in pattern
        if letter == pattern[num]:
            num+=1
        #if you're finished with the pattern then finish ahead of time
        if num > len(pattern)-1:
            return True
        
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    num = 0     #index to keep track of which letter in pattern you're comparing to you
    index = 0
    if len(pattern) == 0:
        return index
    for x in range(len(text)):
        print(num)
        print(text[x])
        print(pattern[num])
        print(index)
        #if they arent equal and you're part of the way into comapring to the pattern
        if num>0 and text[x] != pattern[num]:
            num = 0         #reset the num counter
            index = 0       #reset the index counter
        # check if your current letter matches a letter in pattern
        if text[x] == pattern[num]:
            if num == 0:
                index = x
            num+=1
        #if you're finished with the pattern then finish ahead of time
        if num > len(pattern)-1:
            return index
    
    return None



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    index = []
    for t in range(len(text)):
        #if your pattern is an empty string
        if len(pattern) == 0:
            index.append(t)
            continue
        print("iteration: ", t, text[t])
        # check if your current letter matches a letter in pattern
        if text[t] == pattern[0]:
            index.append(t)     #add index of the first character
            x = t               #temp var to iterate using the current t
            #loop over the rest of the word to see if
            for y in range(len(pattern)):
                #if not equal it means it isnt a full pattern
                print(text[x])
                print(pattern[y])
                if text[x] != pattern[y]:
                    print("deleted")
                    del index[len(index)-1]     #delete the index from indexes because the pattern is broken
                    break
                #is equal but reached end of text and pattern hasnt ended yet
                elif x==len(text)-1 and y<len(pattern)-1:
                    print("deleted bc end of text")
                    del index[len(index)-1]     #delete the index from indexes because the pattern is broken
                    break
                if x<len(text)-1:
                    x+=1
            print("end of pattern search")

    return index
    


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


print(find_all_indexes('ababc', 'abc'))
