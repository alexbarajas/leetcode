import io

def count(needle, haystack):
    """
    :param needle: (String) The text to search for
    :param haystack: (StringIO) An in-memory stream for text I/O
    :returns: (int) The number of lines that contain the needle
    """
    if len(needle) > len(haystack.getvalue()):
        return None
    else:
        left = 0
        right = len(needle)
        matches = 0
        while right != len(haystack.getvalue()):
            if needle == haystack.getvalue()[left:right]:
                matches += 1
            left += 1
            right += 1
        return matches

stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
print(count('there', stream))
stream.close()

stream = io.StringIO("Hello, there!")
print(count('there', stream))
stream.close()

stream = io.StringIO("Hello, thee!")
print(count('there', stream))
stream.close()

# THIS DID NOT WORK FOR ALL CASES