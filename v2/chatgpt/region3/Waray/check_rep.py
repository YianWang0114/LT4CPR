import pdb
from collections import defaultdict
from pathlib import Path
import os
# senList = ['200']

repeated = {}
sent = []
directory = Path.cwd()
files = os.listdir(str(directory)+'/raw')
for s in files:
    with open(str(directory)+'/raw/'+str(s)) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip('\n')
            if (l not in sent):
                sent.append(l)
            else:
                if (l not in repeated):
                    repeated[l] = 1
                else:
                    repeated[l] +=1


with open('repeated.txt', "w") as f2:
    for key, value in repeated.items():
        f2.writelines(key+"\t"+str(value)+'\n')