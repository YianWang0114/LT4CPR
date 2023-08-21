import pdb

lines = open('IBM.txt').readlines()
result = []
for l in lines:
    if ('name' in l):
        lang = l.split(':')[1].strip('\n').strip(' ').strip('"')
        result.append(lang)
with open("IBMtrans.txt", 'w') as f:
    for i in result:
        f.writelines(i+'\n')
