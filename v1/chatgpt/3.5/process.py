import pdb
with open('Bemba.txt') as f:
    lines = f.readlines()
with open('Bemba_after.txt', "w") as f2:
    for sent in lines:
        after = sent.split('\t')[1].split('(')[0].replace("'","")
        f2.writelines(after+'\n')
