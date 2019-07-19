import re
import collections

# 1. Получите текст из файла.
with open('bbdf098ff5cb54f973d0c3b6d9b736e3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Разбейте полученные текст на предложения.
sentences = re.split(r'[\.!\?]\s', text)
print(sentences)

# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
words = re.findall(r'[a-zA-Zа-яА-Я]{4,}', text)
wordsDict = {}
for word in words:
    if word in wordsDict:
        wordsDict[word] += 1
    else:
        wordsDict[word] = 1
cnt = collections.Counter(words)
print(cnt.most_common(10))

# 4. Отберите все ссылки.
links_pattern = re.compile(r'(?:\w+\.)+\w+\/?\w+')
links = links_pattern.findall(text)
print(links)

# 5. Ссылки на страницы какого домена встречаются чаще всего?
domains_pattern = re.compile(r'(?:\w+\.)+\w+')
domains = domains_pattern.findall(text)
cnt = collections.Counter(domains)
print(cnt.most_common(1)[0][0])

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации»
text = links_pattern.sub('<Ссылка отобразится после регистрации>', text)
print(text)
