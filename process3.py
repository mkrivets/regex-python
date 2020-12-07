

import re
import codecs


# help(re)
with codecs.open('input.txt', 'r', 'utf-8') as fin:
    contents = fin.read()

pattern = re.compile(r'\b[a-zA-Zа-яА-ЯієїІЄЇ0-9\'`_-]{1,26}\s*(;|:|\?)\s*[0-9]+\.[0-9]\s*(;|:|\?)\s*[0-9]+\.[0-9]{4}\s*(;|:|\?)\s*[1-9][0-9]*\s*(;|:|\?)\s*[0-9a-zA-Z]{13}\s*(;|:|\?)\s*[0-9]+\.[0-9]+\s*(;|:|\?)\s*(шт.|кг|м|кор.)')
matches = pattern.finditer(contents)
fout = codecs.open('result.txt', 'w', 'utf-8')
for match in matches:
    fout.write(match.group())
    fout.write('\n')
