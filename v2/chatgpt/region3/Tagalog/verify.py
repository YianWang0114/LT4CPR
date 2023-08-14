import os
import pdb
from pathlib import Path


 
# iterate over files in
# that directory
directory = Path.cwd()
files = os.listdir(str(directory)+'/verification')
result = []
for filename in os.listdir(str(directory)+'/verification'):
    with open(str(directory)+'/verification/'+filename) as f:
        lines = f.readlines()
    try:
        assert (len(lines) == 100 or len(lines) == 200)
    except:
        print("assert error")

    correct = 0
    incorrect = 0
    for l in lines:
        if ("Filipino" not in l and "Tagalog" not in l):
            incorrect += 1
        else:
            correct += 1

    assert (incorrect + correct == len(lines))
    result.append([filename, correct, incorrect])

with open('result.txt', "w") as f:
  f.writelines("filename\tcorrect\tincorrect\taccuracy\t\n")
  for r in result:
    f.writelines(r[0]+'\t'+str(r[1])+'\t'+str(r[2])+'\t'+'\t'+str(r[1]/(r[1]+r[2]))+'\n')
