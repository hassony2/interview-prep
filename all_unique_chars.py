def test_all_unique(chars):
    all_unique = True
    known_chars = {}
    for char in chars:
        if char in known_chars:
            all_unique = False
            break
        else:
            known_chars[char] = True
    return all_unique

if __name__ == "__main__":
    test1 = "this has repetitions"
    test2 = "abcdeffghijkl"
    test3 = "abcdefghijklmnop"
    print(test1, ' has all unique chars is ', test_all_unique(test1))
    print(test2, ' has all unique chars is ', test_all_unique(test2))
    print(test3, ' has all unique chars is ', test_all_unique(test3))
