# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
import random

def shuffle(to_shuffle):
    """Implements Fisher-Yates algorithm"""
    for idx in range(len(to_shuffle) - 1):
        # Careful ! randint returns indexes **including** bounds
        rand_idx = random.randint(idx+1, len(to_shuffle) - 1)  
        to_shuffle[idx], to_shuffle[rand_idx] = to_shuffle[rand_idx], to_shuffle[idx]
    return to_shuffle
