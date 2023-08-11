import pdb
from collections import defaultdict
langList = ['Bemba','Bicolano','Bisaya','Chavacano','Hiligaynon','Ilokano','Kapampangan','Maranao', 'Pangasinan',
            'Portuguese','Tagalog', 'Waray-Waray']
repeated = []
for l in langList:
    with open( l + '.txt') as f:
        lines = f.readlines()
        senset = set(lines)
        if (len(senset) != len(lines)):
            print("Repeated sentence")
            for i in lines:
                count = lines.count(i)
                if (count > 1):
                    if (l+' : '+i not in repeated):
                        repeated.append(l+' : '+i)

with open('repeated.txt', "w") as f2:
    for r in repeated:
       f2.writelines(r) 

correct_rate = []
for l in langList:
    langcount = defaultdict(lambda:0)
    with open( l + '_verify.txt') as f:
        lines = f.readlines()
        for i in lines:
            if (i != ''):
                lang = i.split('(')[1].strip('\n').strip(')')
                langcount[lang] += 1
        correct_rate.append(langcount)


with open('correct_rate.txt', "w") as f2:
    for r in correct_rate:
        maxcount = 0
        totalcount = 0
        for k,v in r.items():
            f2.writelines(k+':'+str(v)+'\n')
            maxcount = max(maxcount,v)
            totalcount += v

        f2.writelines("Correct rate: " + str(maxcount/totalcount*100)+'\n\n')