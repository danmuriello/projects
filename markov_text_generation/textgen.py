# markov-probability based text generator

f = open("lotr.txt","rb")
content = f.read()

bag = {}

import re, random

raw = re.findall('[a-zABCDEFGHIJKLMNOQRSTUVWXYZ,\-.\']+',content)
for i in raw:
    if i not in bag:
        bag[i] = []

previous = ''
for i in raw:
    if previous != '':
        bag[previous].append(i)
    previous = i

starters = re.findall('\.\s+[0-9:]*\s*([a-zABCDEFGHIJKLMNOQRSTUVWXYZ]+)',content)


this = random.choice(starters)
sentence = this
for x in range(5000):
    next = random.choice(bag[this])
    if next in ['gogogadgetdano','talktotim']:
        sentence += '\n'+ next + ' '
    else:
        sentence += ' '+ next
    this = next
print sentence

f.close()
