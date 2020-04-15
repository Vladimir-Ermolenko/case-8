"""Case-study #6 Генерация предложений
Разработчики:
Шарков К.(95%), , Ермоленко В. (10%)
"""

# importing the module that gives an opportunity to use a randomized value
import random

# the list of all the symbles
cor_symb = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '.', ',', '?', '!', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# getting all the needed info from the user
filename = input('Введите название файла(файл должен быть в ANSI, программа может работать с английским текстом):')
n = int(input('Введите количество желаемых предложений:'))
lines = []

# getting a list of strings in a file
with open(filename) as dict_file:
    first_lst = dict_file.read()
lines = first_lst.split()
new = []

# getting a list of consecutive words
for word in lines:
    for symbol in word:
        if symbol.lower() not in cor_symb:
            word = word[:word.find(str(symbol))] + word[1 + word.find(str(symbol)):]
    new.append(word)

# removing unneeded symbols
while True:
    try:
        new.remove('')
    except ValueError:
        break

# getting a list of capitalized words
start_words = []
for word in new:
    if word.istitle():
        start_words.append(word)

# making a list that contents the keys
spsp = []
for word in range(len(new) - 1):
    chet = 0
    for i in range(len(spsp)):
        if new[word] == spsp[i][0]:
            if new[word + 1] not in spsp[i] and not new[word + 1].istitle():
                spsp[i].append(new[word + 1])  # spsp - list of lists, the zero word of each sublist is the key
            chet = 1
    if chet == 0 and not (new[word].endswith('.') or new[word].endswith('!') or new[word].endswith('?')):
        spsp.append([new[word], new[word + 1]])


# the main function that generates the text itsels
def gener(start_words, spsp):
    predloj = []
    st = start_words[random.randrange(0, len(start_words), 1)]
    predloj.append(st)

    for all in range(len(spsp)):
        if spsp[all][0] == st:
            rand = random.randrange(1, len(spsp[all]), 1)
            word = spsp[all][rand]
            predloj.append(word)

    while not (predloj[len(predloj) - 1].endswith('.') or predloj[len(predloj) - 1].endswith('!') or
               predloj[len(predloj) - 1].endswith('?')) and len(predloj) < 19:
        for all in range(len(spsp)):
            if spsp[all][0] == word:
                rand = random.randrange(1, len(spsp[all]), 1)
                newword = spsp[all][rand]
                predloj.append(newword)
        word = newword

    if not (predloj[len(predloj) - 1].endswith('.') or predloj[len(predloj) - 1].endswith('!') or
            predloj[len(predloj) - 1].endswith('?')):
        lastword = str(predloj.pop) + '.'
        predloj.append(lastword)

    if 4 < len(predloj) < 20:
        return predloj
    else:
        return gener(start_words, spsp)

def main():
    for i in range(n):
        print(' '.join(gener(start_words, spsp)), end=' ')

main()
