from noun import Noun
from verb import Verb
from sentense import Sentense

words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))
words.append(Verb("ехал"))
words.append(Noun("дорога"))
words.append(Verb("моет"))
words.append(Noun("солнце"))

sentense = Sentense()
sentense.content = [0, 1, 5, 6]

print(sentense.show(words))
print(sentense.show_parts(words))