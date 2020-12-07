
import re
import codecs

with codecs.open('input.txt', 'r', 'utf-8') as fin:
    contents = fin.read()

result = re.sub(r'\s*[;:?]\s*', ' ; ', contents)

result = re.sub(r' ; (шт.|кг|м|кор.)', '', result)

fout = codecs.open('result.txt', 'w', 'utf-8')
fout.write(result)
fout.close()
