
import sys

dico_tyler = {} # GLOBAL dictionnaries
dico_jack = {}

def fill_dico(words_found, charac):
    for word in words_found:
        if word != 'TYLER:' and word != '--' and word != 'JACK:' and word != 'JACK' and word != '(V.O.):':
            word2 = word.replace('.', '')
            word2 = word2.replace(',', '')
            word2 = word2.replace('!', '')
            word2 = word2.replace('?', '')
            word2 = word2.replace('…', '') # different than '...'
            word2 = word2.lower()
            if charac == 'tyler':
                dico_tyler[word2] = 1
            elif charac == 'jack':
                dico_jack[word2] = 1



count_dial_tyler = 0
count_dial_jack = 0

tylers_words = 0


count_characters = 0
count_characters_nospace = 0

with open(sys.argv[1], 'r') as filein:
    for line in filein:
        word_list = line.split()
        if line[0:6] == 'TYLER:':
            count_dial_tyler+=1
            tylers_words+=len(word_list)
            tylers_words-=1 # Remove "TYLER:"
            fill_dico(word_list, 'tyler')

        elif line[0:5] == 'JACK:':
            count_dial_jack+=1
            fill_dico(word_list, 'jack')

        elif line[0:12] == 'JACK (V.O.):':
            count_dial_jack+=1
            fill_dico(word_list, 'jack')

        else:
            length = len(line)
            if length > 1: # discard empty line (the 1 char is the newline)
                count_characters+=length # newlines are counted
                line_nospace = line.replace(' ', '')
                count_characters_nospace+=len(line_nospace)

print("Jack a",count_dial_jack, "répliques.")
print("Tyler a",count_dial_tyler, "répliques.")
print("Tyler prononce",tylers_words, "mots, au total.")
print("Tyler prononce",len(dico_tyler.keys()), "mots différents.")

print("Les lignes de description de la scène contiennent", count_characters, "caractères.")
print("Sans compter les espaces, les lignes de description de la scène contiennent", count_characters_nospace, "caractères.")

common_dico = {}
exclusive_dico = {}

for word_jack in dico_jack.keys():
    if word_jack in dico_tyler:
        common_dico[word_jack] = 1
for word_tyler in dico_tyler.keys():
    if word_tyler in dico_jack:
        common_dico[word_tyler] = 1
    else:
        exclusive_dico[word_tyler] = 1

print("Mots prononcés par les deux personnages :")
for word in common_dico.keys():
    print(word)

print("Mots prononcés exclusivement par Tyler :")
for word in exclusive_dico.keys():
    print(word)
