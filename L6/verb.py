from word import Word


class Verb(Word):
    _grammar = 'гл'

    def part(self):
        return 'глагол'
