class Sentense:
    content = []

    def show(self, words):
        return ' '.join([words[c].text for c in self.content])

    def show_parts(self, words):
        return list(dict.fromkeys([words[c].part() for c in self.content]))
