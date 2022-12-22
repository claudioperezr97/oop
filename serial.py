"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.next = start
        self.start = start

    def generate(self):
        next = self.next
        self.next = self.next + 1
        return next

    def reset(self):
        self.next = self.start


if __name__ == "__main__":
    import doctest
    doctest.testmod()
