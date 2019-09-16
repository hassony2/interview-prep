from collections import Counter
from shuffling import shuffle
from matplotlib import pyplot as plt

def test_shuffle():
    card_nb = 4
    shuffle_nb = 100000
    to_shuffle = list(range(card_nb))
    shuffledlists = [tuple(shuffle(to_shuffle)) for idx in range(shuffle_nb)]
    counter = Counter(shuffledlists)
    print(list("{}: {}".format(shuffle, counts/shuffle_nb) for shuffle, counts in counter.items()))
    plt.bar(list(range(len(counter))), counter.values())
    plt.show()

test_shuffle()

