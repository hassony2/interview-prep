def get_non_repeating_chars(in_stream):
    """
    Given an input stream of n characters consisting
    only of small case alphabets the task is to find
    the first non repeating character each time a character
    is inserted to the stream.

    Example :
    "a a b c" --> "a -1 b b"
    """
    chars = in_stream.split(" ")
    chars = [char_ for char_ in chars if char_ is not '']
    solo_chars = []
    encountered_chars = {}
    out_chars = []
    for char_ in chars:
        if char_ in encountered_chars:
            occurences = encountered_chars[char_]
            if occurences == 1:
                print(solo_chars)
                solo_chars.remove(char_)
            encountered_chars[char_] = occurences + 1
        else:
            encountered_chars[char_] = 1
            solo_chars.append(char_)
        print(solo_chars)
        if(solo_chars):
            out_chars.append(solo_chars[0])
        else:
            out_chars.append('-1')
        print(out_chars)
    out_stream = ' '.join(out_chars)
    return out_stream

if __name__ == "__main__":
    stream = "a a b c d "
    stream = "b t r w b l n s a d e u g u u m o q c d r u b\
              e t o k y x h o a c h w d v m x x r d r y x l m n d\
              q t u k w a g m l e j u u k w "
    expected = "a -1 b b b c"
    print(get_non_repeating_chars(stream))
    print(expected)
