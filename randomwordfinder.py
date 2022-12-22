from wordfinder import WordFinder
import random


class RandomWordFinder(WordFinder):

    def __init__(self):
        super().__init__()
        self.words = self.remove()

    def remove(self):
        return list(filter(self.contains, self.words))

    def random(self):
        idx = random.randint(0, len(self.words) - 1)
        print(idx)
        return self.words[idx]

    def contains(self, str):
        if '#' in str or (not str):
            return False
        return True


word_finder = RandomWordFinder()
print(word_finder.random())
