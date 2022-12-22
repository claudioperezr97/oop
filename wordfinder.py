"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:

    def __init__(self):
        words = list(open('words2.txt', 'r'))
        self.words = [word.strip() for word in words]
        print(f"{len(self.words)} words read.")

    def random(self):
        idx = random.randint(0, len(self.words) - 1)
        print(self.words[idx])
        return self.words[idx]
