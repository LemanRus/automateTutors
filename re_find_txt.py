from pathlib import Path
import re

exp = input('Введите регулярку:\n')
rexp = r'{}'.format(exp)

for file in Path.glob(Path.cwd(), '*.txt'):
    text = file.read_text(encoding='utf-8')
    print(re.findall(rexp, text))
