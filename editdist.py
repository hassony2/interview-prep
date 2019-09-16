def bruteforce_mindist(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    if word2[0] == word1[0]:
        return bruteforce_mindist(word1[1:], word2[1:])
    else:
        # Min of 3 possibilities: delete, insert, replace
        return 1 + min(bruteforce_mindist(word1[1:], word2), bruteforce_mindist(word1, word2[1:]), bruteforce_mindist(word1[1:], word2[1:]))

def dyn_mindist(word1, word2, mem={}, start_word1=0, start_word2=0):
    """
    gets minimum edit distance from word1[start_word1:] and word2[start_word2:]
    saves previous states in mem
    """
    # Reached the end of word1: dist is remainder of word2
    if len(word1) == start_word1:
        return len(word2) - start_word2
    # Reached the end of word2: dist is remainder of word1
    elif len(word2) == start_word2:
        return len(word1) - start_word1
    if (start_word1, start_word2) in mem:
        # Return pre-computed dist
        return mem[(start_word1, start_word2)]
    else:
        # Next letter matches, optimal to continue without increasing dist
        if word1[start_word1] == word2[start_word2]:
            new_dist = dyn_mindist(word1, word2, mem, start_word1 + 1, start_word2 +1)
        else:
            # Mismatch !
            # Delete <=> skip first letter from word1
            # Insert <=> skip first letter from word2
            # Replace <=> skip letters from both words
            # and continue
            new_dist = 1 + min(dyn_mindist(word1, word2, mem, start_word1 + 1, start_word2), dyn_mindist(word1, word2, mem, start_word1, start_word2 + 1), dyn_mindist(word1, word2, mem, start_word1 + 1, start_word2 + 1))
        mem[(start_word1, start_word2)] = new_dist
        return new_dist

if __name__ == "__main__":
    word_pairs = [("asfddfs", ""), ("ab", "a"), ("aejrlk", "ljdksf")]
    for word1, word2 in word_pairs:
        print("Dist from {} to {} is {} (brute) {} (dyn)".format(word1, word2, bruteforce_mindist(word1, word2), dyn_mindist(word1, word2)))
