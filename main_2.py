import os

files_name = 'FILE'
file_path = os.path.join(os.getcwd(), files_name)
files = os.listdir(file_path)
file_dict = {}
for file in files:
    name = os.path.join(file_path, file)
    with open(name, 'rt', encoding='utf-8') as f:
        data = f.readlines()
        file_dict[len(data)] = name
dict_sort = {k: v for k, v in sorted(file_dict.items(), key=lambda item: item[0])}


with open('sort.txt', 'w', encoding='utf-8') as file:
    for k, v in dict_sort.items():
        with open(v, 'rt', encoding='utf-8') as f:
            name_txt = os.path.basename(v)
            file.write(f'{name_txt}\n {k}\n {"".join(f).strip()}\n')
