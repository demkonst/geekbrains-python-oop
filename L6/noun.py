from word import Word


class Noun(Word):
    _grammar = 'сущ'

    def part(self):
        return 'существительное'
