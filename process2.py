
import re
import codecs

with codecs.open('input.txt', 'r', 'utf-8') as fin:
    contents = fin.read()

result = re.sub(r'\s*[;:?]\s*', ' ; ', contents)

result = re.sub(r'; \b(шт\.|кг|м|кор\.)\s*', '', result)

fout = codecs.open('result.txt', 'w', 'utf-8')
fout.write(result)
fout.close()
