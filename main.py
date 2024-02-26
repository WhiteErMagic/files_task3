
f_dict = {}

with open('1.txt', 'r', encoding='utf-8') as f1:
    f_dict[f1.name] = sum(1 for line in f1)

with open('2.txt', 'r', encoding='utf-8') as f2:
    f_dict[f2.name] = sum(1 for line in f2)

with open('3.txt', 'r', encoding='utf-8') as f3:
    f_dict[f3.name] = sum(1 for line in f3)

with open('all.txt', 'w', encoding='utf-8') as f_all:
    for k, v in sorted(f_dict.items(), key=lambda item: item[1]):
        f_all.write(k+'\n')
        f_all.write(str(v)+'\n')
        with open(k, 'r', encoding='utf-8') as f_:
            while True:
                line = f_.readline()
                if not line:
                    break
                f_all.write(line)
        f_all.write('\n')