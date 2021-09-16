
from os import replace


def read_referat():
    with open ('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        return content

print(read_referat())
print(len(read_referat()))
def point_on_exclamation_mark(txt):
    return txt.replace('.', '!')

print(point_on_exclamation_mark(read_referat()))

def writer_referat(text):
    with open ('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        print('файл записан.')

writer_referat(point_on_exclamation_mark(read_referat()))