
import re
import codecs

regex1 = re.compile(r'[0-9]+\.[0-9]+\s*(;|:|\?)\s*[0-9a-zA-Z]{15}\s*(;|:|\?)\s*(шт\.|кг|м|кор\.)\s*(;|:|\?)\s*[a-zA-Zа-яА-Я0-9ієїІЄЇ\'_-]{1,25}\s*(;|:|\?)\s*[0-9]+\.[0-9]{2}\s*(;|:|\?)\s*[1-9]{1}[0-9]*\s*(;|:|\?)\s*[0-9]+\.[0-9]{2}')

with codecs.open('input.txt', 'r', 'utf-8') as fin:
    text = fin.read()

res = re.sub(r'[;:?]', ';', text)
regex = re.compile(r'.+\s*;\s*.+\s*;\s*.+\s*;\s*.+\s*;\s*0\.00\s*;\s*.+\s*;\s*.+')
matches = regex.finditer(res)
fout = codecs.open('result.txt', 'w', 'utf-8')
for match in matches:
    fout.write(match.group())
    fout.write('\n')


