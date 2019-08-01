# п.п. 1, 2
class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part


# п.3
w = Word('сделать', 'глагол')


# п.п. 4, 5
class Sentense:
    content = []

    # п.7
    def show(self, words):
        return ' '.join([words[c].text for c in self.content])

    # п.8
    def show_parts(self, words):
        return list(dict.fromkeys([words[c].part for c in self.content]))


rawWords = [["я", "местоимение"],
            ["выглянул", "глагол"],
            ["в", "предлог"],
            ["окно", "существительное"],
            ["и", "союз"],
            ["увидел", "глагол"],
            ["что", "союз"],
            ["метель", "существительное"],
            ["разбушевалась", "глагол"]]

# п.6
words = [Word(word[0], word[1]) for word in rawWords]

sentense = Sentense()
sentense.content = [0, 1, 5, 6]

print(sentense.show(words))
print(sentense.show_parts(words))
