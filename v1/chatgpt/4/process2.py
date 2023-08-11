import pdb
# with open('Bemba.txt') as f:
#     lines = f.readlines()
# with open('Bemba_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split('\t')[1].split('-')[0].replace("'","")
#         f2.writelines(after+'\n')
    

# with open('Tagalog.txt') as f:
#     lines = f.readlines()
# with open('Tagalog_after.txt', "w") as f2:
#     for sent in lines:
#         if (sent != '\n'):
#             after = sent.split('(')[0].strip()
#             f2.writelines(after+'\n')

# with open('Bisaya.txt') as f:
#     lines = f.readlines()
# with open('Bisaya_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split(' - ')[0].strip()
#         f2.writelines(after+'\n')

# with open('Hiligaynon.txt') as f:
#     lines = f.readlines()
# with open('Hiligaynon_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split('(')[0].strip()
#         f2.writelines(after+'\n')

# with open('Waray-Waray.txt') as f:
#     lines = f.readlines()
# with open('Waray-Waray_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split(' - ')[0].strip()
#         f2.writelines(after+'\n')


# with open('Kapampangan.txt') as f:
#     lines = f.readlines()
# with open('Kapampangan_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split('(')[0].strip()
#         f2.writelines(after+'\n')

# with open('Bicolano.txt') as f:
#     lines = f.readlines()
# with open('Bicolano_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split('(')[0].strip()
#         f2.writelines(after+'\n')


# with open('Pangasinan.txt') as f:
#     lines = f.readlines()
# with open('Pangasinan_after.txt', "w") as f2:
#     for sent in lines:
#         after = sent.split(' - ')[0].strip()
#         f2.writelines(after+'\n')

with open('Maranao.txt') as f:
    lines = f.readlines()
with open('Maranao_after.txt', "w") as f2:
    for sent in lines:
        after = sent.split('(')[0].strip()
        f2.writelines(after+'\n')